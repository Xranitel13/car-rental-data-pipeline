import subprocess
import sys


def run_step(command: list[str], step_name: str) -> None:
    print(f"\nRunning step: {step_name}")

    result = subprocess.run(command, check=False)

    if result.returncode != 0:
        raise RuntimeError(f"Step failed: {step_name}")

    print(f"Finished step: {step_name}")


def main():
    run_step(
        [sys.executable, "-m", "car_rental_gcp_data_platform.prepare_raw_data"],
        "Prepare raw vehicle and branch data",
    )

    run_step(
        [sys.executable, "-m", "car_rental_gcp_data_platform.generate_transactions"],
        "Generate transactional data",
    )

    run_step(
        [sys.executable, "-m", "car_rental_gcp_data_platform.load_to_duckdb"],
        "Load raw data to DuckDB",
    )

    run_step(
        [
            "dbt",
            "build",
            "--project-dir",
            "dbt/car_rental_dbt",
            "--profiles-dir",
            "dbt",
        ],
        "Run dbt models and tests",
    )


if __name__ == "__main__":
    main()