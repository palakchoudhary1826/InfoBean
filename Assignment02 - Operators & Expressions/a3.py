'''
========================================
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0
'''

totalBill=int(input("Enter the Total Bill Amount :- "))
totalFriends=int(input("Enter The Total Number Of Freinds :- "))
split=int(totalBill/totalFriends)
print(" ")
print("Total Bill :-",totalBill)
print("Friends :-",totalFriends)
print("Each Should Pay :-",split)