import module.inventor

product = []

for i in range(1, 6):

    pro_id = int(input("Enter the product id: "))

    pro_name = input("Enter the product name: ")

    price = int(input("Enter the product price: "))

    quantity = int(input("Enter the quantity: "))

    pro = module.inventor.Product(pro_id, pro_name, price, quantity)

    product.append(pro)


print("------ Display All Products -------")

for i in product:
    i.display()


print("------- Total Value ------")

for i in product:

    total = i.price * i.quantity

    print(i.product_name, "=", total)


print("---- Quantity is Less Than 10 -----------")

for i in product:

    if i.quantity < 10:
        i.display()


print("--------- Highest Price ---------")

high = product[0]

for i in product:

    if i.price > high.price:
        high = i

high.display()


print("------- Total Inventory Value -------")

total = 0

for i in product:

    total += i.price * i.quantity

print(total)


print("--------- Search Product ---------")

search = int(input("Enter the search product id: "))

for i in product:

    if i.product_id == search:
        i.display()