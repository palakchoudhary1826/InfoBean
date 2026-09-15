'''
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0

'''
cp=int(input("Enter The Cost Price : "))
sp=int(input("Enter The Selling Price : "))
print(f"Profit : {sp-cp}")
print(f"Profit in % : {((sp-cp)/cp)*100} %")
