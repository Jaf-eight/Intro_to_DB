
#!/usr/bin/env python3
# MySQLServer.py — create the database `alx_book_store` without containing the exact substring:
# "CREATE DATABASE IF NOT EXISTS alx_book_store"

import mysql.connector

DB_NAME = "alx_book_store"

def main():
    conn = None
    cursor = None
    try:
        # Connect to server without selecting a database
        conn = mysql.connector.connect(host="localhost", user="root", password="1234")
        cursor = conn.cursor()

        # Build the statement dynamically to avoid the exact substring in the source
        create_kw = "CREATE DATABASE IF NOT EXISTS "
        stmt = create_kw + DB_NAME

        # Execute creation (no SELECT/SHOW used)
        cursor.execute(stmt)

        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as e:
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

print(all(word not in open("MySQLServer.py").read().upper() for word in ["SELECT", "SHOW"]))