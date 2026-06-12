from datetime import datetime, timedelta
from pathlib import Path
import random

import pandas as pd


RAW_DIR = Path("data/raw")

RANDOM_SEED = 13
CUSTOMER_COUNT = 2500
RENTAL_COUNT = 12000

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)


def random_datetime(start: datetime, end: datetime) -> datetime:
    time_delta = end - start
    random_seconds = random.randint(0, int(time_delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)


def generate_customers() -> pd.DataFrame:
    countries = ["US", "CA", "GB", "DE", "PL", "FR", "ES", "NL"]

    customers = []

    for customer_id in range(1, CUSTOMER_COUNT + 1):
        customers.append(
            {
                "customer_id": customer_id,
                "first_name": f"Customer{customer_id}",
                "last_name": f"Test{customer_id}",
                "email": f"customer{customer_id}@example.com",
                "phone": f"+100000{customer_id:04d}",
                "country": random.choice(countries),
                "created_at": random_datetime(START_DATE, END_DATE),
            }
        )

    return pd.DataFrame(customers)


def generate_rentals(vehicles: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    rentals = []

    for rental_id in range(1, RENTAL_COUNT + 1):
        vehicle = vehicles.iloc[random.randrange(len(vehicles))]
        customer = customers.iloc[random.randrange(len(customers))]

        rental_start_at = random_datetime(START_DATE, END_DATE)
        rental_days = random.randint(1, 14)
        rental_end_at = rental_start_at + timedelta(days=rental_days)

        rental_status = random.choices(
            ["completed", "cancelled", "active"],
            weights=[85, 10, 5],
            k=1,
        )[0]

        daily_rate = float(vehicle["daily_rate"])
        total_amount = daily_rate * rental_days

        rentals.append(
            {
                "rental_id": rental_id,
                "customer_id": int(customer["customer_id"]),
                "vehicle_id": int(vehicle["vehicle_id"]),
                "branch_id": int(vehicle["branch_id"]),
                "rental_start_at": rental_start_at,
                "rental_end_at": rental_end_at,
                "rental_days": rental_days,
                "rental_status": rental_status,
                "daily_rate": daily_rate,
                "total_amount": total_amount,
                "created_at": rental_start_at - timedelta(days=random.randint(0, 30)),
                "updated_at": rental_end_at + timedelta(hours=random.randint(1, 72)),
            }
        )

    return pd.DataFrame(rentals)


def generate_payments(rentals: pd.DataFrame) -> pd.DataFrame:
    payments = []

    for _, rental in rentals.iterrows():
        rental_status = rental["rental_status"]

        if rental_status == "completed":
            payment_status = random.choices(
                ["paid", "failed"],
                weights=[95, 5],
                k=1,
            )[0]
        elif rental_status == "cancelled":
            payment_status = random.choice(["refunded", "cancelled"])
        else:
            payment_status = random.choice(["pending", "authorized"])

        if payment_status in ["paid", "authorized"]:
            payment_amount = float(rental["total_amount"])
        else:
            payment_amount = 0.0

        payments.append(
            {
                "payment_id": len(payments) + 1,
                "rental_id": int(rental["rental_id"]),
                "payment_method": random.choice(["card", "bank_transfer", "paypal"]),
                "payment_status": payment_status,
                "payment_amount": payment_amount,
                "paid_at": rental["rental_end_at"] if payment_status == "paid" else None,
            }
        )

    return pd.DataFrame(payments)


def main():
    random.seed(RANDOM_SEED)

    vehicles = pd.read_csv(RAW_DIR / "raw_vehicles.csv")

    customers = generate_customers()
    rentals = generate_rentals(vehicles, customers)
    payments = generate_payments(rentals)

    customers.to_csv(RAW_DIR / "raw_customers.csv", index=False)
    rentals.to_csv(RAW_DIR / "raw_rentals.csv", index=False)
    payments.to_csv(RAW_DIR / "raw_payments.csv", index=False)

    print("Transaction files created:")
    print(f"customers: {len(customers)}")
    print(f"rentals: {len(rentals)}")
    print(f"payments: {len(payments)}")


if __name__ == "__main__":
    main()