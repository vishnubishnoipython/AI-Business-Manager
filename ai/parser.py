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

    # ================= TYPE DETECTION =================

    expense_keywords = [
        "diesel",
        "petrol",
        "rent",
        "salary",
        "electricity",
        "office",
        "fuel",
        "internet",
        "mobile",
        "repair",
        "maintenance"
    ]

    # Payment
    if (
        "payment" in message
        or "paid" in message
        or "jama" in message
        or "payment ki" in message
        or "paisa diya" in message
        or "paise diye" in message
    ):
        data["type"] = "payment"

    # Sale
    elif (
        "ko" in message
        and (
            "diya" in message
            or "diye" in message
        )
    ) or "sold" in message:
        data["type"] = "sale"

    # Purchase
    elif (
        "kharida" in message
        or "kharide" in message
        or "purchase" in message
        or "buy" in message
    ):
        data["type"] = "purchase"

    # Expense
    else:
        for word in expense_keywords:
            if word in message:
                data["type"] = "expense"
                break

    # ================= PRODUCT =================

    for product in products:
        if product.lower() in message:
            data["product"] = product.title()
            break

    # ================= NUMBERS =================

    numbers = re.findall(r"\d+", message)

    # ================= QUANTITY & AMOUNT =================

    # Sale / Purchase
    if data["type"] in ["sale", "purchase"]:

        qty = re.search(
            r"(\d+)\s*(kg|bag|bags|ton|tons|pcs|piece|pieces)",
            message
        )

        if qty:
            data["quantity"] = int(qty.group(1))

        if len(numbers) >= 2:
            data["amount"] = int(numbers[-1])

    # Payment
    elif data["type"] == "payment":

        data["quantity"] = 0

        if numbers:
            data["amount"] = int(numbers[0])

    # Expense
    elif data["type"] == "expense":

        data["quantity"] = 0

        if numbers:
            data["amount"] = int(numbers[0])

    # ================= CUSTOMER =================

    if data["type"] == "sale":

        words = message.split()

        if len(words) > 0:
            data["customer"] = words[0].title()

    elif data["type"] == "purchase":

        data["customer"] = "Supplier"

    elif data["type"] == "payment":

        words = message.split()

        if len(words) > 0:
            data["customer"] = words[0].title()

    else:

        data["customer"] = ""

    return data