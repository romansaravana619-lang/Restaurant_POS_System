import sqlite3

DB_PATH = r"D:\SARU SYSTEMS\02_Projects\Restaurant_POS_System\04_Database\database\restaurant_pos.db"


def main():
    connection = sqlite3.connect(DB_PATH)

    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS dining_sessions (
                session_id TEXT PRIMARY KEY,
                customer_id TEXT NOT NULL,
                table_id TEXT NOT NULL,
                status TEXT NOT NULL,
                started_at TEXT NOT NULL,
                closed_at TEXT,

                FOREIGN KEY (customer_id)
                    REFERENCES customers(customer_id),

                FOREIGN KEY (table_id)
                    REFERENCES restaurant_tables(table_id)
            )
            """
        )

        connection.commit()

        print("dining_sessions table created successfully.")
        print(
            connection.execute(
                "SELECT sql FROM sqlite_master "
                "WHERE type='table' AND name='dining_sessions'"
            ).fetchone()[0]
        )

    finally:
        connection.close()


if __name__ == "__main__":
    main()
