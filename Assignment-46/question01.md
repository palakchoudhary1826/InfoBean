"""============================================================
QUESTION 1: ONLINE PAYMENT MANAGEMENT SYSTEM
============================================================

Develop a MENU-DRIVEN Online Payment Management System for an
e-commerce company.

The company supports different payment methods:

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Every payment method follows a common payment process, but the
actual validation, authentication, processing fee and payment
processing logic are different.

Therefore, the system must be designed using ABSTRACTION.

------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------

Create an abstract class named:

Payment

The class should define the following abstract methods:

1. validate_payment()
2. calculate_processing_fee()
3. authenticate_payment()
4. process_payment()
5. generate_receipt()

Create separate child classes for:

1. UPIPayment
2. CreditCardPayment
3. DebitCardPayment
4. NetBankingPayment
5. WalletPayment

Each child class must provide its own implementation of all
required abstract methods.

------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit

Enter your choice:

------------------------------------------------------------
OPTION 1: MAKE PAYMENT
------------------------------------------------------------

Ask the user to enter:

Customer Name
Order ID
Order Amount

Then display:

Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Enter your choice:

------------------------------------------------------------
UPI:
------------------------------------------------------------

Input:

UPI ID
UPI PIN

Processing Fee:

0%

------------------------------------------------------------
CREDIT CARD:
------------------------------------------------------------

Input:

Card Number
Card Holder Name
CVV
Expiry Date

Processing Fee:

2% of Order Amount

------------------------------------------------------------
DEBIT CARD:
------------------------------------------------------------

Input:

Card Number
Card Holder Name
CVV
Expiry Date

Processing Fee:

1% of Order Amount

------------------------------------------------------------
NET BANKING:
------------------------------------------------------------

Input:

Bank Name
Account Number
Customer ID

Processing Fee:

0.5% of Order Amount

------------------------------------------------------------
WALLET:
------------------------------------------------------------

Input:

Wallet Name
Mobile Number
Wallet PIN

Processing Fee:

1.5% of Order Amount

------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------

Enter Customer Name: Rahul
Enter Order ID: ORD1052
Enter Order Amount: 5000

Select Payment Method:

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Enter your choice: 2

Enter Card Number: 4567891234567890
Enter Card Holder Name: Rahul Singh
Enter CVV: 321
Enter Expiry Date: 12/29

------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------

========================================
          PAYMENT PROCESSING
========================================

Customer Name       : Rahul
Order ID            : ORD1052
Payment Method      : Credit Card

Order Amount        : Rs.5000.00
Processing Fee      : Rs.100.00
Final Amount        : Rs.5100.00

Validating payment details...
Payment details validated successfully.

Authenticating payment...
Authentication successful.

Processing payment...
Payment processed successfully.

Transaction ID      : TXN785421
Payment Status      : SUCCESS

========================================

OPTION 2: VIEW PAYMENT DETAILS
------------------------------------------------------------

Ask:

Enter Order ID:

If the order exists, display:

Order ID
Customer Name
Payment Method
Order Amount
Processing Fee
Final Amount
Transaction ID
Payment Status

If the order does not exist:

Payment record not found.

OPTION 3:

Display:

Thank you for using Online Payment System"""