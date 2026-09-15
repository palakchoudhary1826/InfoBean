"""
=========================================
9. INVENTORY MANAGEMENT SYSTEM
=========================================

Store product stock in a dictionary.

stock = {
    "Pen": 50,
    "Pencil": 100,
    "Eraser": 25,
    "Marker": 10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
"""

n = int(input("Enter The No. of Products : "))

d = {}
p = {}

for i in range(n):
    product, stock = input(
        "Enter Product Name and Stock : "
    ).split()

    d[product] = d.get(product, 0) + int(stock)

print("Product Dictionary :")
print(d)

for k, v in d.items():
    if v <=30:
        p[k] = v

print("Stock Which Is Less Than 30  :")

for k, v in p.items():
    print(f"{k} : {v}")