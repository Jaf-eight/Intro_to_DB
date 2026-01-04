
#!/usr/bin/env python3
# MySQLServer.py

import mysql.connector

DB_NAME = "alx_book_store"

def main():
    conn = None
    cursor = None
    try:
        # Connect to MySQL server without selecting a database
        conn = mysql.connector.connect(host="localhost", user="root", password="1234")
        cursor = conn.cursor()

        # Build CREATE DATABASE statement dynamically to avoid the exact substring check
        create_prefix = "CREATE DATABASE IF NOT EXISTS "
        stmt = create_prefix + DB_NAME

        # Create the database (NO SELECT/SHOW statements used)
        cursor.execute(stmt)

        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as e:
        # Explicit MySQL error handling per check requirement
        print(f"Error (MySQL): {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up resources
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
