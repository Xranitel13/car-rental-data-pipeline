from pathlib import Path

import pandas as pd


EXTERNAL_FILE = Path("data/external/CarRentalDataV1.csv")
RAW_DIR = Path("data/raw")


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(EXTERNAL_FILE)

    df = df.rename(columns={
        "fuelType": "fuel_type",
        "renterTripsTaken": "renter_trips_taken",
        "reviewCount": "review_count",
        "location.city": "location_city",
        "location.country": "location_country",
        "location.latitude": "location_latitude",
        "location.longitude": "location_longitude",
        "location.state": "location_state",
        "owner.id": "owner_id",
        "rate.daily": "daily_rate",
        "vehicle.make": "vehicle_make",
        "vehicle.model": "vehicle_model",
        "vehicle.type": "vehicle_type",
        "vehicle.year": "vehicle_year",
        "airportcity": "airport_city",
    })

    branch_key = [
        "location_city",
        "location_country",
        "location_state",
        "airport_city",
    ]

    branches = (
        df
        .groupby(branch_key, dropna=False, as_index=False)
        .agg(
            location_latitude=("location_latitude", "mean"),
            location_longitude=("location_longitude", "mean"),
        )
        .reset_index(drop=True)
    )

    branches.insert(0, "branch_id", range(1, len(branches) + 1))

    vehicles = df.merge(
        branches[branch_key + ["branch_id"]],
        on=branch_key,
        how="left",
    )

    vehicles = vehicles[
        [
            "fuel_type",
            "rating",
            "renter_trips_taken",
            "review_count",
            "owner_id",
            "daily_rate",
            "vehicle_make",
            "vehicle_model",
            "vehicle_type",
            "vehicle_year",
            "branch_id",
        ]
    ].copy()

    vehicles.insert(0, "vehicle_id", range(1, len(vehicles) + 1))

    branches.to_csv(RAW_DIR / "raw_branches.csv", index=False)
    vehicles.to_csv(RAW_DIR / "raw_vehicles.csv", index=False)

    print("Raw files created:")
    print(f"branches: {len(branches)}")
    print(f"vehicles: {len(vehicles)}")


if __name__ == "__main__":
    main()