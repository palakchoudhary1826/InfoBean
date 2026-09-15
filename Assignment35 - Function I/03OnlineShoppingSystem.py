def display():
    print("\n" + "*" * 40)
    print("        ONLINE SHOPPING SYSTEM")
    print("*" * 40)

    print("""
1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit
""")

def customerRegister(name,email,mobile):
    print("Customer register Successfully")
    print(f"Name  :{name}")
    print(f"Email :{email}")
    print(f"Mobile:{mobile}")

def productInfo(pname,price,category):
    print("Product Details ")
    print(f"Product Name : {pname}")
    print(f"Product Price : {price}")
    print(f"Product Category : {category}")

def generateInvoice(name,price,tax=18):
    taxAmt=(price*tax)/100
    finalAmt=price+taxAmt
    print()
    print("*"*30)
    print("Invoice")
    print("*"*30)
    print()
    print(f"Product Name    : {name}")
    print(f"Product Price   : {price}")
    print(f"Tax Percentage  : {tax}%")
    print(f"Tax Amount      : {taxAmt}")
    print(f"Final Amount    : {finalAmt}")
    print("Invoice Generated Successfull")


def calculateTotal(*prices):
    sum=0
    for i in prices:
        sum+=i
    print(f"Total Bill Amount : {sum}")

def profile(**detail):
    print("Customer profile fetched")

    for k,v in detail.items():
        print(k,":",v)

while True:

    display()

    choice = int(input("Enter Choice : "))

    match choice:

        case 1:
            print("Customer Registration")
            name=input("Enter Name    : ")
            email=input("Enter Email  :")
            mobile=input("Enter Mobile : ")
            #positional
            customerRegister(name,email,mobile)
            

        case 2:
            print("Product Information")
            Pname=input("Enter Product Name    : ")
            price=input("Enter Price  :")
            category=input("Enter Category : ")
            productInfo(pname=Pname,price=price,category=category)


        case 3:
            print("Generate Invoice")
            pname=input("Enter Product Name  : ")
            price=input("Enter Product Price : ")
            generateInvoice(pname,int(price))

        case 4:
            print("Add Multiple Products")
            n=int(input("Enter Number Of Product : "))
            prices=[]
            for i in range(n):
                price=int(input(f"Enter Price {i+1} : "))
                prices.append(price)

            calculateTotal(*prices)
            

        case 5:
            print("Display Customer Profile")
            name=input("Enter Name : ")
            city=input("Enter city : ")
            email=input("Enter email : ")
            mobile=input("Enter mobile : ")
            membership=input("Enter membership : ")

            profile(
                Name=name,City=city,Email=email,Mobile=mobile,MembershipType=membership
            )



        case 6:
            break

        case _:
            print("Invalid Choice")