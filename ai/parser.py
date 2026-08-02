print("AI Parser Loaded Successfully")

import re


def parse_message(message, products):

    message = message.lower()

    data = {
        "type": "unknown",
        "customer": "",
        "product": "",
        "quantity": 0,
        "amount": 0
    }

    # Quantity
    qty = re.search(r"(\d+)\s*(kg|bag|bags|ton|pcs|piece)?", message)

    if qty:
        data["quantity"] = int(qty.group(1))

    # Amount
    amount = re.findall(r"\d+", message)

    if len(amount) >= 2:
        data["amount"] = int(amount[-1])

    # Customer
    words = message.split()

    if len(words) > 0:
        data["customer"] = words[0].title()

    # Product Detection
    for product in products:
        if product.lower() in message:
            data["product"] = product.title()
            break

    # Sale Detection
    if "diya" in message or "diye" in message:
        data["type"] = "sale"

    return data