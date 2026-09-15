"""
QUESTION 4: ONLINE SHOPPING ORDERS

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

2. Display all order details.

3. Find and display the order having the highest amount.

4. Calculate and display total sales.

5. Count the number of orders whose amount is greater than ₹10,000.

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
"""

from collections import namedtuple


order=namedtuple("order",["order_id","customer_name","product_name","amount"])


n=int(input("Enter The Number of Orders : "))
list=[]


for i in range(n):
    print(f"Enter Order {i+1} Details")
    id=input("Enter Order ID       : ")
    name=input("Enter Customer Name  : ")
    product=input("Enter Product Name   : ")
    amount=input("Enter Amount         : ")
    list.append(order(id,name,product,int(amount)))
    print(f"{i+1}th Order Details Stored ...")
    print()


print(list)


print("All Order Details : ")


count=1


for i in list:
    print(f"{count}th Order Details")
    print(f"Order ID       : {i.order_id}")
    print(f"Customer Name  : {i.customer_name}")
    print(f"Product Name   : {i.product_name}")
    print(f"Amount         : {i.amount}")
    count+=1
    print()


highest=list[0]
total=0
count=0

for i in list:
    if i.amount>highest.amount:
        highest=i

    total+=i.amount

    if i.amount>10000:
        count+=1


print("Highest Value Order : ")
print(f"Order ID       : {highest.order_id}")
print(f"Customer Name  : {highest.customer_name}")
print(f"Product Name   : {highest.product_name}")
print(f"Amount         : {highest.amount}")


print()
print(f"Total Sales : {total}")


print()
print(f"Orders Above ₹10,000 : {count}")