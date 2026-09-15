'''
Docstring for a03

 Smart Banking System

Scenario:
You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

👉 Important Condition:
If no amount has been deposited yet, the system should display:
"No balance available. Please deposit first"
and should not allow withdrawal, balance check, or interest calculation.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest

* Balance > 50000 → 5% interest
* Otherwise → 3% interest
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
No balance available. Please deposit first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter amount to deposit: 10000

Output:
Amount deposited successfully

---

Sample Run 3:
Input:
Enter your choice: 3

Output:
Current Balance: 10000

---

Sample Run 4:
Input:
Enter your choice: 2
Enter amount to withdraw: 15000

Output:
Insufficient balance

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
Interest added: 300
Updated Balance: 10300

---

Sample Run 6:
Input:
Enter your choice: 2
Enter amount to withdraw: 5000

Output:
Withdrawal successful

---

Sample Run 7 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 8 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!
'''

print("=" * 55)
print("               BANK ACCOUNT SYSTEM")
print("=" * 55)

balance = 0
interest = 0

while True:

    print("\nMAIN MENU")
    print("-" * 55)
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Exit")
    print("-" * 55)

    choice = int(input("Enter your choice : "))
    print()

    match choice:

        case 1:
            amount = int(input("Enter Deposit Amount : ₹"))

            if amount > 0:
                balance += amount

                print("\nDEPOSIT SUCCESSFUL")
                print("-" * 35)
                print(f"Deposited Amount : ₹{amount}")
                print(f"Current Balance  : ₹{balance}")
            else:
                print("Invalid Amount!")

        case 2:
            if balance > 0:

                amount = int(input("Enter Withdrawal Amount : ₹"))

                if amount <= 0:
                    print("Invalid Amount!")

                elif balance >= amount:
                    balance -= amount

                    print("\nWITHDRAWAL SUCCESSFUL")
                    print("-" * 35)
                    print(f"Withdrawn Amount : ₹{amount}")
                    print(f"Remaining Balance: ₹{balance}")

                else:
                    print("Insufficient Balance.")

            else:
                print("No balance available. Please deposit money first.")

        case 3:
            print("\nACCOUNT BALANCE")
            print("-" * 35)
            print(f"Available Balance : ₹{balance}")

        case 4:

            if balance > 0:

                if balance > 50000:
                    rate = 5
                else:
                    rate = 3

                interest = balance * rate // 100
                balance += interest

                print("\nINTEREST APPLIED")
                print("-" * 35)
                print(f"Interest Rate    : {rate}%")
                print(f"Interest Earned  : ₹{interest}")
                print(f"Updated Balance  : ₹{balance}")

            else:
                print("No balance available. Please deposit money first.")

        case 5:
            print("\n" + "=" * 55)
            print("      THANK YOU FOR USING OUR BANKING SYSTEM")
            print("             Program Closed Successfully")
            print("=" * 55)
            break

        case _:
            print(" Invalid Choice! Please try again.")

    print("\n" + "*" * 55)