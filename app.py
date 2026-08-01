from flask import Flask, render_template, request
from database.db import (
    create_database,
    save_sale,
    get_all_sales,
    get_sale_by_id,
    update_sale,
    delete_sale,
    get_total_sales
    )

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    total_sales = get_total_sales()

    return render_template(
        "index.html",
        total_sales=total_sales
    )


@app.route("/add-sale", methods=["GET", "POST"])
def add_sale():

    if request.method == "POST":
        customer = request.form["customer"]
        product = request.form["product"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        save_sale(customer, product, quantity, price)

        return f"""
        <h2>Sale Saved Successfully ✅</h2>

        <p><b>Customer:</b> {customer}</p>
        <p><b>Product:</b> {product}</p>
        <p><b>Quantity:</b> {quantity}</p>
        <p><b>Price:</b> ₹{price}</p>

        <br>
        <a href="/add-sale">Add Another Sale</a>
        <br><br>
        <a href="/">Back to Dashboard</a>
        """

    return render_template("add_sale.html")


@app.route("/view-sales")
def view_sales():

    sales = get_all_sales()

    return render_template("view_sales.html", sales=sales)
@app.route("/edit-sale/<int:sale_id>", methods=["GET", "POST"])
def edit_sale(sale_id):

    sale = get_sale_by_id(sale_id)

    if request.method == "POST":
        customer = request.form["customer"]
        product = request.form["product"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        update_sale(sale_id, customer, product, quantity, price)

        return """
        <h2>Sale Updated Successfully ✅</h2>
        <br>
        <a href="/view-sales">Back to View Sales</a>
        """

    return render_template("edit_sale.html", sale=sale)
@app.route("/delete-sale/<int:sale_id>")
def delete_sale_route(sale_id):

    delete_sale(sale_id)

    return """
    <h2>Sale Deleted Successfully ✅</h2>

    <br>

    <a href="/view-sales">Back to View Sales</a>
    """
if __name__ == "__main__":
    app.run(debug=True)