import sqlite3


DATABASE_NAME = "coffee_machine.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (

            order_id TEXT PRIMARY KEY,

            coffee_name TEXT,

            quantity INTEGER,

            total REAL

        )
    """)

    connection.commit()

    connection.close()


def save_order(
    order_id,
    coffee_name,
    quantity,
    total
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO orders
        (order_id, coffee_name, quantity, total)

        VALUES (?, ?, ?, ?)
    """, (
        order_id,
        coffee_name,
        quantity,
        total
    ))

    connection.commit()

    connection.close()


def get_orders():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM orders"
    )

    orders = cursor.fetchall()

    connection.close()

    return orders