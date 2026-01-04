
#!/usr/bin/env python3
"""
MySQLServer.py
Creates the database `alx_book_store` and its tables on a MySQL server.
- Does not fail if the database already exists.
- Prints success message when database is created.
"""

import mysql.connector
from mysql.connector import Error



try:
    # Connect to MySQL server (without selecting a database yet)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"  # Change to your MySQL password
    )

    cursor = conn.cursor()
    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

    # Switch to the database
    cursor.execute("USE alx_book_store")

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INT AUTO_INCREMENT PRIMARY KEY,
        author_name VARCHAR(215) NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(215) NOT NULL,
        email VARCHAR(215) NOT NULL,
        address TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(130) NOT NULL,
        author_id INT NOT NULL,
        price DOUBLE NOT NULL,
        publication_date DATE,
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT NOT NULL,
        order_date DATE NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Order_Details (
        orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT NOT NULL,
        book_id INT NOT NULL,
        quantity DOUBLE NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
    """)

except Error as e:
    print(f"Error: {e}")
finally:

    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
#except mysql.connector.Error

#!/usr/bin/env python3
# MySQLServer.py — create the database `alx_book_store` safely and briefly

import mysql.connector

DB_NAME = "alx_book_store"

def main():
    conn = None
    cursor = None
    try:
        # Connect to server without selecting a database
        conn = mysql.connector.connect(host="localhost", user="root", password="1234")
        cursor = conn.cursor()

        # Create DB (won’t fail if it already exists); no SELECT/SHOW used
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

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
