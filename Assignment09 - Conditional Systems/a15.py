'''
Docstring for Assignment09.a15
E-Commerce Dynamic Pricing System

An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.

If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%
'''

demand = int(input("Enter Demand: "))
stock = int(input("Enter Stock: "))
user_type = input("Enter User Type (premium/regular): ").lower()
festival = input("Is it Festival Season? (yes/no): ").lower()
d=""
if demand>=80:
    if stock<50:
        if user_type=="premium":
            if festival=="yes":
                d="20%"
            else:
                d="10%"
        else:
            d="no discount"
    elif stock>=50:
        d="5% discount"
elif demand>=40 and demand<=79:
    if festival=="yes":
        d="10%"
    else:
        d="no discount"

else:
    if demand<40:
        if stock>200:
           d="15%"
        else:
           d="no discount"
           

print(f"Discount :{d}")
           
