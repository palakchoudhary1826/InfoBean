'''
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
'''

totalBill=int(input("Enter The Bill Amount : "))
friends=int(input("Enter The Number Of Friends:- "))
gst=int(input("Enter The GST :- "))
charge=int(input("Enter The Service Charge :-"))


gstOnBill=(totalBill/100)*gst
serviceCharge=(totalBill/100)*charge

finalBill=gstOnBill+totalBill+serviceCharge

print(f"Final Bill : {finalBill}")
print(f"Each Person Pays : {finalBill/friends}")