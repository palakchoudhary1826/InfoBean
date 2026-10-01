
def main():
    print("""
========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit""")


def display2():
    customer_name=input("enter the customer name:")
    oredr_id=int(input("enter the order id:"))
    order_amout=int(input("enter the order amount:"))
    

def main2():
    print("""1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet
""")

    
    
while True:
    main()
    choice=int(input("enter your choice:"))
    match choice:
        case 1:
            display2()
    print("select payment method")
    while True:
        main2()
        choice=int(input("enter the choice:"))
        match choice:
            case 1:
                upi_id=int(input("enter your upi id:"))
                upi_pin=int(input("enter your upi pin:"))
                processing_fees=0
            case 2:
                card_num=int(input("enter your card number:"))
                card_holder_name=input("enter your card holder name:")
                cvv=int(input("enter your cvv number":))
                expiry_date=int(input("enter your expiry date:"))
                processing_fees=2
            case 3:
                card_num=int(input("enter your card number:"))
                card_holder_name=input("enter your card holder name:")
                cvv=int(input("enter your cvv number:"))
                expiry_date=int(input("enter your expiry date:"))
                processing_fees=1
            case 4:
                bank_name=input("enter your bank name:")
                account_num=int(input("enter your account num:"))
                customer_id=int(input("enter your customer id:"))
                fees_processing=0.5

            case 5:
                wallet_name=input("enter your wallet name:")
                mobile_num=int(input("enter your mobile num:"))
                wallet_pin=int(input("enter your wallet pin:"))
                processing_fees=1.5
            






