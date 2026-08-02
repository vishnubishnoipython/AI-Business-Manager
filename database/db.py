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
    # Product Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        category TEXT,
        purchase_price REAL,
        selling_price REAL,
        stock INTEGER
    )
""")
    # Customer Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        mobile TEXT,
        email TEXT,
        gst TEXT,
        address TEXT
    )
""")
    conn.commit()
    conn.close()

def add_date_columns():

    print("Checking date columns...")

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "ALTER TABLE sales ADD COLUMN date TEXT"
        )
        print("Sales date column added ✅")

    except Exception as e:
        print("Sales date error:", e)


    try:
        cursor.execute(
            "ALTER TABLE expenses ADD COLUMN date TEXT"
        )
        print("Expenses date column added ✅")

    except Exception as e:
        print("Expenses date error:", e)


    conn.commit()
    conn.close()

# ---------------- SALES ---------------- #

def save_sale(customer, product, quantity, price, date):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales 
        (customer, product, quantity, price, date)
        VALUES (?, ?, ?, ?, ?)
    """,
    (customer, product, quantity, price, date))

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

    cursor.execute(
        "SELECT * FROM sales WHERE id = ?",
        (sale_id,)
    )

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
    """,
    (customer, product, quantity, price, sale_id))

    conn.commit()
    conn.close()


def delete_sale(sale_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sales WHERE id=?",
        (sale_id,)
    )

    conn.commit()
    conn.close()


def get_total_sales():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(price) FROM sales")

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0



# ---------------- EXPENSES ---------------- #

def save_expense(category, description, amount):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses(category, description, amount)
        VALUES (?, ?, ?)
    """,
    (category, description, amount))

    conn.commit()
    conn.close()



def get_all_expenses():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    conn.close()

    return rows



def get_expense_by_id(expense_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE id=?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    conn.close()

    return expense



def update_expense(expense_id, category, description, amount):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET category=?, description=?, amount=?
        WHERE id=?
    """,
    (category, description, amount, expense_id))

    conn.commit()
    conn.close()



def delete_expense(expense_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    conn.commit()
    conn.close()



def get_total_expenses():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0
    
def get_profit():

    total_sales = get_total_sales()
    total_expenses = get_total_expenses()

    profit = total_sales - total_expenses

    return profit

    # ---------------- PRODUCTS ---------------- #

def save_product(product_name, category, purchase_price, selling_price, stock):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products
        (product_name, category, purchase_price, selling_price, stock)
        VALUES (?, ?, ?, ?, ?)
    """, (
        product_name,
        category,
        purchase_price,
        selling_price,
        stock
    ))

    conn.commit()
    conn.close()


def get_all_products():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_product_by_id(product_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE id=?",
        (product_id,)
    )

    product = cursor.fetchone()

    conn.close()

    return product


def update_product(
    product_id,
    product_name,
    category,
    purchase_price,
    selling_price,
    stock
):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE products
        SET
            product_name=?,
            category=?,
            purchase_price=?,
            selling_price=?,
            stock=?
        WHERE id=?
    """, (
        product_name,
        category,
        purchase_price,
        selling_price,
        stock,
        product_id
    ))

    conn.commit()
    conn.close()


def delete_product(product_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id=?",
        (product_id,)
    )

    conn.commit()
    conn.close()


def save_customer(customer_name, mobile, email, gst, address):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers
        (customer_name, mobile, email, gst, address)
        VALUES (?, ?, ?, ?, ?)
    """, (
        customer_name,
        mobile,
        email,
        gst,
        address
    ))
def get_all_customers():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")

    rows = cursor.fetchall()

    conn.close()

    return rows
    conn.commit()
    conn.close()