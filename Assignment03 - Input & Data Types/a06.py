'''
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
'''
amount=int(input("Enter The Amount : "))
discount=amount*(10/100)
print(f"Amount : {amount}")
print(f"Discount :{discount}")
print(f"Final : {amount-discount}")