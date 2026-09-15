'''

7. Banking Withdrawal Limit System


A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000
'''

b=int(input("Enter The balance : "))

if b<1000:
    print("withdrawal not allowed")
elif b<=5000:
    print("max withdrawal limit 1000")
else:
    print("Maximum withdrawal ₹5000")
    
