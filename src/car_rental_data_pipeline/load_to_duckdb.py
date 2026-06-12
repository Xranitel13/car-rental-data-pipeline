from pathlib import Path

import duckdb
import pandas as pd


RAW_DIR = Path("data/raw")
WAREHOUSE_DIR = Path("data/warehouse")
DATABASE_FILE = WAREHOUSE_DIR / "car_rental.duckdb"

RAW_TABLES = {
    "raw_branches": "raw_branches.csv",
    "raw_vehicles": "raw_vehicles.csv",
    "raw_customers": "raw_customers.csv",
    "raw_rentals": "raw_rentals.csv",
    "raw_payments": "raw_payments.csv",
}


def main():
    WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

    connection = duckdb.connect(DATABASE_FILE)

    for table_name, file_name in RAW_TABLES.items():
        file_path = RAW_DIR / file_name

        df = pd.read_csv(file_path)

        connection.register("temp_df", df)

        connection.execute(
            f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT *
            FROM temp_df
            """
        )

        row_count = connection.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        ).fetchone()[0]

        print(f"Loaded {table_name}: {row_count} rows")

    connection.close()

    print(f"DuckDB database created: {DATABASE_FILE}")


if __name__ == "__main__":
    main()