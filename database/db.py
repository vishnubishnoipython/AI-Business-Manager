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
    # Stock Ledger Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_ledger(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        transaction_type TEXT,
        quantity INTEGER,
        balance_stock INTEGER,
        remarks TEXT,
        date TEXT
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

def get_product_names():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT product_name FROM products")

    rows = cursor.fetchall()

    conn.close()

    products = []

    for row in rows:
        products.append(row[0].lower())

    return products

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

def reduce_stock(product_name, sold_quantity):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM products
        WHERE LOWER(product_name)=LOWER(?)
    """, (product_name,))

    product = cursor.fetchone()

    if product:

        current_stock = product[5]

        new_stock = current_stock - sold_quantity

        if new_stock < 0:
            new_stock = 0

        cursor.execute("""
            UPDATE products
            SET stock=?
            WHERE id=?
        """, (
            new_stock,
            product[0]
        ))

    conn.commit()
    conn.close()

def increase_stock(product_name, purchase_quantity):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM products
        WHERE LOWER(product_name)=LOWER(?)
    """, (product_name,))

    product = cursor.fetchone()

    if product:

        current_stock = product[5]

        new_stock = current_stock + purchase_quantity

        cursor.execute("""
            UPDATE products
            SET stock=?
            WHERE id=?
        """, (
            new_stock,
            product[0]
        ))

    conn.commit()
    conn.close()
def get_current_stock(product_name):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT stock
        FROM products
        WHERE LOWER(product_name)=LOWER(?)
    """, (product_name,))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return 0
def save_stock_ledger(
    product,
    transaction_type,
    quantity,
    balance_stock,
    remarks,
    date
):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO stock_ledger
        (
            product,
            transaction_type,
            quantity,
            balance_stock,
            remarks,
            date
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        product,
        transaction_type,
        quantity,
        balance_stock,
        remarks,
        date
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
def get_customer_by_id(customer_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE id=?",
        (customer_id,)
    )

    customer = cursor.fetchone()

    conn.close()

    return customer


def update_customer(
    customer_id,
    customer_name,
    mobile,
    email,
    gst,
    address
):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE customers
        SET
            customer_name=?,
            mobile=?,
            email=?,
            gst=?,
            address=?
        WHERE id=?
    """, (
        customer_name,
        mobile,
        email,
        gst,
        address,
        customer_id
    ))

    conn.commit()
    conn.close()
def delete_customer(customer_id):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE id=?",
        (customer_id,)
    )

    conn.commit()
    conn.close()
def get_stock_ledger():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM stock_ledger
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows