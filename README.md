# Car Rental Data Pipeline

A local data engineering project for practicing Python, SQL, DuckDB and dbt.

The project uses a public car rental dataset and synthetic transaction data to build a small ELT pipeline with raw, staging, intermediate and mart layers.

## Goal

The goal of this project is to practice building a structured analytical pipeline:

* prepare raw data with Python
* load data into a local DuckDB warehouse
* transform data with dbt
* create simple analytical marts
* add basic data quality tests

## Pipeline

```text
External CSV dataset
        ↓
Python data preparation
        ↓
Synthetic transaction generation
        ↓
DuckDB local warehouse
        ↓
dbt staging models
        ↓
dbt intermediate model
        ↓
dbt mart tables
        ↓
dbt tests
```

## Tech Stack

* Python
* Poetry
* pandas
* DuckDB
* dbt
* dbt-duckdb

## Data

The project combines:

* a public car rental dataset for vehicle and location data
* synthetic customer, rental and payment data generated with Python

Raw tables:

* `raw_vehicles`
* `raw_branches`
* `raw_customers`
* `raw_rentals`
* `raw_payments`

## dbt Models

Staging models:

* `stg_vehicles`
* `stg_branches`
* `stg_customers`
* `stg_rentals`
* `stg_payments`

Intermediate model:

* `int_rental_financials`

Mart models:

* `mart_daily_revenue`
* `mart_branch_performance`
* `mart_vehicle_utilization`

## Data Quality

The project includes basic dbt tests for:

* not-null values
* unique IDs
* relationships between tables
* accepted rental and payment statuses

## How to Run

Install dependencies:

```bash
poetry install
```

Run the full local pipeline:

```bash
poetry run python -m car_rental_gcp_data_platform.run_pipeline
```

Or run steps manually:

```bash
poetry run python -m car_rental_gcp_data_platform.prepare_raw_data
poetry run python -m car_rental_gcp_data_platform.generate_transactions
poetry run python -m car_rental_gcp_data_platform.load_to_duckdb
poetry run dbt build --project-dir dbt/car_rental_dbt --profiles-dir dbt
```

## Output

After running the pipeline, a local DuckDB database is created:

```text
data/warehouse/car_rental.duckdb
```

It contains:

* raw tables
* staging views
* intermediate view
* mart tables

To inspect created database objects:

```bash
poetry run python -m car_rental_gcp_data_platform.check_warehouse
```

## Project Structure

```text
car-rental-gcp-data-platform/
├── data/
│   ├── external/
│   ├── raw/
│   └── warehouse/
│
├── src/
│   └── car_rental_gcp_data_platform/
│       ├── prepare_raw_data.py
│       ├── generate_transactions.py
│       ├── load_to_duckdb.py
│       ├── check_warehouse.py
│       └── run_pipeline.py
│
├── dbt/
│   ├── profiles.yml
│   └── car_rental_dbt/
│       └── models/
│           ├── staging/
│           ├── intermediate/
│           └── marts/
│
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Notes

DuckDB is used as a local warehouse so the project can be run without cloud costs. The same general structure could later be adapted to BigQuery or another cloud data warehouse.

## Status

* [x] Raw data preparation
* [x] Synthetic transaction generation
* [x] DuckDB loading
* [x] dbt staging models
* [x] dbt intermediate model
* [x] dbt mart models
* [x] dbt tests
* [x] Local pipeline runner
