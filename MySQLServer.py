
#!/usr/bin/env python3
"""
MySQLServer.py
Creates the database `alx_book_store` on a MySQL server.
- Does not fail if the database already exists.
- No SELECT or SHOW statements used.
- Prints success message when created.
"""

import mysql.connector
from mysql.connector import Error

DB_NAME = "alx_book_store"

try:
    # Connect to MySQL server (without specifying a database yet)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"  # Change to your MySQL password
    )

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully!")
except Error as e:
    print(f"Error: {e}")
finally:
    # Close resources
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
