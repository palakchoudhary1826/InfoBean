"""
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
"""


n=int(input("Enter The Number of Products : "))
list=[]


for i in range(n):
    print(f"Enter Product {i+1} Details")
    id=input("Enter Product ID       : ")
    name=input("Enter Product Name     : ")
    price=input("Enter Price            : ")

    product=(id,name,int(price))
    list.append(product)

    print(f"{i+1}th Product Details Stored ...")
    print()


print("All Product Details : ")

for i in list:
    print(i)


costliest=list[0]
cheapest=list[0]
sum=0

for i in list:
    if i[2]>costliest[2]:
        costliest=i

    if i[2]<cheapest[2]:
        cheapest=i

    sum+=i[2]


print("Costliest Product : ")
print(costliest)


print("Cheapest Product : ")
print(cheapest)


print(f"Average Price : {sum/n}")


print("Products Above ₹50,000 : ")

for i in list:
    if i[2]>50000:
        print(i)