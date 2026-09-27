def calculate_total(cart, coffees):

    total = 0

    for coffee_name, quantity in cart.items():

        price = coffees[coffee_name]["price"]

        item_total = price * quantity

        total = total + item_total

    return total


def check_payment(total, amount):

    if amount >= total:

        change = amount - total

        return True, change

    else:

        return False, 0