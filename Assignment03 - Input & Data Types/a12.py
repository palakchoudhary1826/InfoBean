'''

Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3

'''
amt=int(input("Enter The Amount : "))
hundred=amt//100;
remain1=amt%100;
fifty=remain1//50;
remain2=remain1%50;
ten=remain2//10;

print(f"100rs x {hundred}\n50rs x {fifty}\n10rs x {ten}")