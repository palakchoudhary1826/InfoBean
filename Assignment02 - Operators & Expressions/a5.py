'''
========================================
Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240

'''
print("12% GST is applied on a cart")

cartBill=int(input("Enter Your Cart Value :- "))
tax=int(cartBill*(12/100))
totalBill=cartBill+tax;
print(" ")
print(f"Cart : {cartBill} rupees" )
print(f"Tax : {tax} rupees")
print(f"Total :{totalBill} rupees")
