from flask import Flask, render_template, request
print("APP FILE LOADED")
from database.db import (
    create_database,
    add_date_columns,

    # Sales
    save_sale,
    get_all_sales,
    get_sale_by_id,
    update_sale,
    delete_sale,
    get_total_sales,

    # Expenses
    save_expense,
    get_all_expenses,
    get_expense_by_id,
    update_expense,
    delete_expense,
    get_total_expenses,
    get_profit,
    
    # Products
    save_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
)

app = Flask(__name__)

create_database()
# add_date_columns()

@app.route("/")
def home():

    total_sales = get_total_sales()
    total_expenses = get_total_expenses()
    profit = get_profit()

    return render_template(
        "index.html",
        total_sales=total_sales,
        total_expenses=total_expenses,
        profit=profit
    )



# ---------------- SALES ---------------- #

@app.route("/add-sale", methods=["GET", "POST"])
def add_sale():

    if request.method == "POST":

        customer = request.form["customer"]
        product = request.form["product"]
        quantity = request.form["quantity"]
        price = request.form["price"]
        date = request.form["date"]

        save_sale(customer, product, quantity, price,date)

        return """
        <h2>Sale Saved Successfully ✅</h2>
        <br>
        <a href="/add-sale">Add Another Sale</a>
        <br><br>
        <a href="/">Dashboard</a>
        """

    return render_template("add_sale.html")



@app.route("/view-sales")
def view_sales():

    sales = get_all_sales()

    return render_template(
        "view_sales.html",
        sales=sales
    )



@app.route("/edit-sale/<int:sale_id>", methods=["GET","POST"])
def edit_sale(sale_id):

    sale = get_sale_by_id(sale_id)

    if request.method == "POST":

        customer = request.form["customer"]
        product = request.form["product"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        update_sale(
            sale_id,
            customer,
            product,
            quantity,
            price
        )

        return """
        <h2>Sale Updated Successfully ✅</h2>
        <br>
        <a href="/view-sales">Back</a>
        """

    return render_template(
        "edit_sale.html",
        sale=sale
    )



@app.route("/delete-sale/<int:sale_id>")
def delete_sale_route(sale_id):

    delete_sale(sale_id)

    return """
    <h2>Sale Deleted Successfully ✅</h2>
    <br>
    <a href="/view-sales">Back</a>
    """




# ---------------- EXPENSES ---------------- #


@app.route("/add-expense", methods=["GET","POST"])
def add_expense():

    if request.method == "POST":

        category = request.form["category"]
        description = request.form["description"]
        amount = request.form["amount"]

        save_expense(
            category,
            description,
            amount
        )

        return """
        <h2>Expense Saved Successfully ✅</h2>
        <br>
        <a href="/add-expense">Add Another Expense</a>
        <br><br>
        <a href="/">Dashboard</a>
        """

    return render_template("add_expense.html")



# View Expenses

@app.route("/view-expenses")
def view_expenses():

    expenses = get_all_expenses()

    return render_template(
        "view_expenses.html",
        expenses=expenses
    )



# Edit Expense

@app.route("/edit-expense/<int:expense_id>", methods=["GET","POST"])
def edit_expense(expense_id):

    expense = get_expense_by_id(expense_id)

    print("EDIT EXPENSE DATA:", expense)   # temporary check

    if request.method == "POST":

        category = request.form["category"]
        description = request.form["description"]
        amount = request.form["amount"]

        update_expense(
            expense_id,
            category,
            description,
            amount
        )

        return """
        <h2>Expense Updated Successfully ✅</h2>
        <br>
        <a href="/view-expenses">Back</a>
        """

    return render_template(
        "edit_expense.html",
        expense=expense
    )



# Delete Expense

@app.route("/delete-expense/<int:expense_id>")
def delete_expense_route(expense_id):

    delete_expense(expense_id)


    return """
    <h2>Expense Deleted Successfully ✅</h2>
    <br>
    <a href="/view-expenses">Back to Expenses</a>
    """
# ---------------- PRODUCTS ---------------- #

@app.route("/add-product", methods=["GET", "POST"])
def add_product():

    if request.method == "POST":

        product_name = request.form["product_name"]
        category = request.form["category"]
        purchase_price = request.form["purchase_price"]
        selling_price = request.form["selling_price"]
        stock = request.form["stock"]

        save_product(
            product_name,
            category,
            purchase_price,
            selling_price,
            stock
        )

        return """
        <h2>Product Saved Successfully ✅</h2>

        <br>

        <a href="/add-product">Add Another Product</a>

        <br><br>

        <a href="/">Back to Dashboard</a>
        """

    return render_template("add_product.html")

@app.route("/view-products")
def view_products():

    print("VIEW PRODUCTS ROUTE HIT")
    products = get_all_products()

    return render_template(
        "view_products.html",
        products=products
    )
@app.route("/edit-product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):

    product = get_product_by_id(product_id)

    if request.method == "POST":

        product_name = request.form["product_name"]
        category = request.form["category"]
        purchase_price = request.form["purchase_price"]
        selling_price = request.form["selling_price"]
        stock = request.form["stock"]

        update_product(
            product_id,
            product_name,
            category,
            purchase_price,
            selling_price,
            stock
        )

        return """
        <h2>Product Updated Successfully ✅</h2>

        <br>

        <a href="/view-products">Back to Products</a>
        """

    return render_template(
        "edit_product.html",
        product=product
    )
@app.route("/delete-product/<int:product_id>")
def delete_product_route(product_id):

    delete_product(product_id)

    return """
    <h2>Product Deleted Successfully ✅</h2>

    <br>

    <a href="/view-products">Back to Products</a>
    """
if __name__ == "__main__":
    app.run(debug=True)