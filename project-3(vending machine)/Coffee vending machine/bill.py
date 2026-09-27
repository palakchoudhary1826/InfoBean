import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generate_bill(
    order_id,
    cart,
    coffees,
    total,
    amount,
    change
):

    os.makedirs(
        "bills",
        exist_ok=True
    )

    file_name = (
        f"bills/bill_{order_id}.pdf"
    )

    pdf = canvas.Canvas(
        file_name,
        pagesize=A4
    )

    width, height = A4

    y = height - 60

    # Heading

    pdf.setFont(
        "Helvetica-Bold",
        20
    )

    pdf.drawString(
        180,
        y,
        "COFFEE VENDING MACHINE"
    )

    y -= 40

    # Order ID

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        y,
        f"Order ID: {order_id}"
    )

    y -= 40

    # Table heading

    pdf.setFont(
        "Helvetica-Bold",
        12
    )

    pdf.drawString(
        50,
        y,
        "Coffee"
    )

    pdf.drawString(
        300,
        y,
        "Qty"
    )

    pdf.drawString(
        400,
        y,
        "Price"
    )

    y -= 25

    # Cart items

    pdf.setFont(
        "Helvetica",
        11
    )

    for coffee_name, quantity in cart.items():

        price = coffees[
            coffee_name
        ]["price"]

        item_total = price * quantity

        pdf.drawString(
            50,
            y,
            coffee_name
        )

        pdf.drawString(
            300,
            y,
            str(quantity)
        )

        pdf.drawString(
            400,
            y,
            f"Rs. {item_total}"
        )

        y -= 25

    y -= 20

    pdf.line(
        50,
        y,
        550,
        y
    )

    y -= 30

    pdf.setFont(
        "Helvetica-Bold",
        12
    )

    pdf.drawString(
        50,
        y,
        f"Total: Rs. {total}"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"Paid: Rs. {amount}"
    )

    y -= 25

    pdf.drawString(
        50,
        y,
        f"Change: Rs. {change}"
    )

    y -= 50

    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        200,
        y,
        "Thank You!"
    )

    y -= 25

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        180,
        y,
        "Enjoy your coffee!"
    )

    pdf.save()

    return file_name