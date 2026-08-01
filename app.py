from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-sale", methods=["GET", "POST"])
def add_sale():

    if request.method == "POST":
        customer = request.form["customer"]
        product = request.form["product"]
        quantity = request.form["quantity"]
        price = request.form["price"]

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


if __name__ == "__main__":
    app.run(debug=True)