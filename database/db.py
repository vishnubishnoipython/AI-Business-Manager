import sqlite3

DATABASE_NAME = "database/business.db"


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Sales Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT,
            product TEXT,
            quantity INTEGER,
            price REAL
        )
    """)

    # Expense Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- SALES ---------------- #

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


def get_sale_by_id(sale_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales WHERE id = ?", (sale_id,))
    sale = cursor.fetchone()

    conn.close()

    return sale


def update_sale(sale_id, customer, product, quantity, price):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE sales
        SET customer=?, product=?, quantity=?, price=?
        WHERE id=?
    """, (customer, product, quantity, price, sale_id))

    conn.commit()
    conn.close()


def delete_sale(sale_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sales WHERE id = ?", (sale_id,))

    conn.commit()
    conn.close()


def get_total_sales():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(price) FROM sales")
    total = cursor.fetchone()[0]

    conn.close()

    if total is None:
        return 0

    return total


# ---------------- EXPENSES ---------------- #

def save_expense(category, description, amount):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (category, description, amount)
        VALUES (?, ?, ?)
    """, (category, description, amount))

    conn.commit()
    conn.close()


def get_all_expenses():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    return rows


def get_total_expenses():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()

    if total is None:
        return 0

    return total