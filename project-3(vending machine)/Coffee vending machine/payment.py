
def calculate_total(cart):
     total = 0
     for item in cart:
        amount = item["price"] * item["quantity"]
        total = total + amount
     return total


def check_payment(amount, total):
    if amount >= total:
        change = amount - total
        return True, change
    else:
        remaining = total - amount
        return False, remaining
