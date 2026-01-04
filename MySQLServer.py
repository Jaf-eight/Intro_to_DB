
#!/usr/bin/env python3
# MySQLServer.py

import mysql.connector  # <- required import

DB_NAME = "alxbookstore"  # note: as requested, no underscore

def main():
    conn = None
    cursor = None
    try:
        # Establish connection to MySQL server (no database selected yet)
        conn = mysql.connector.connect(host="localhost", user="root", password="1234")
        cursor = conn.cursor()

        # Create the database if it does not exist (no SELECT/SHOW used)
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

        # (Optional) Set charset/collation without using SELECT/SHOW
        # cursor.execute(f"ALTER DATABASE {DB_NAME} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci")

        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as e:  # explicit MySQL exception handling
        print(f"Error (MySQL): {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
