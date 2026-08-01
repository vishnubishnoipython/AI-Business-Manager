import sqlite3

DATABASE_NAME = "database/business.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            product TEXT,
            quantity INTEGER,
            price REAL
        )
    """)

    conn.commit()
    conn.close()


def save_sale(customer, product, quantity, price):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales (customer, product, quantity, price)
        VALUES (?, ?, ?, ?)
    """, (customer, product, quantity, price))

    conn.commit()
    conn.close()


def get_all_sales():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()

    conn.close()

    return rows