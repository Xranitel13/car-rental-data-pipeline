poetry install
poetry run python -m car_rental_gcp_data_platform.prepare_raw_data
poetry run python -m car_rental_gcp_data_platform.generate_transactions
poetry run python -m car_rental_gcp_data_platform.load_to_duckdb
poetry run dbt debug --project-dir dbt/car_rental_dbt --profiles-dir dbt
poetry run dbt build --project-dir dbt/car_rental_dbt --profiles-dir dbt


poetry run python -m car_rental_gcp_data_platform.check_warehouse
poetry run python -m car_rental_gcp_data_platform.run_pipeline