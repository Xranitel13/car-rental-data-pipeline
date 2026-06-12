import duckdb


def main():
    con = duckdb.connect("data/warehouse/car_rental.duckdb")

    result = con.execute(
        """
        select
            table_schema,
            table_name,
            table_type
        from information_schema.tables
        where table_schema = 'main'
        order by table_type, table_name
        """
    ).fetchdf()

    print(result)


if __name__ == "__main__":
    main()