"""
=========================================
1. ONLINE SHOPPING CART
=========================================

A shopping website stores purchased products in a dictionary where:
Key   = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6
"""


n=int(input("Enter The Number Of Items : "))
d={}

for i in range(n):
    item=input("Enter The Item Name : ")
    quant=int(input("Enter The Quantity : "))
    print()
    d[item]=d.get(item,0)+quant

print(d)

total=0
for i in d.values():
    total+=i

print(f"Total Sum Of Quant  : {total}")

