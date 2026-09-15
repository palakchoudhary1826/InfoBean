'''
Docstring for a04
Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!

'''
print("=" * 60)
print("             ELECTRICITY BILL MANAGEMENT SYSTEM")
print("=" * 60)

isUnit = False
unit = 0
bill = 0
surcharge = 0

while True:

    print("\nMAIN MENU")
    print("-" * 60)
    print("1. Enter Units Consumed")
    print("2. Calculate Bill Amount")
    print("3. Apply Surcharge")
    print("4. Display Final Bill")
    print("5. Exit")
    print("-" * 60)

    choice = int(input("Enter your choice : "))
    print()

    match choice:

        case 1:
            n = int(input("Enter Units Consumed : "))

            if n > 0:
                unit = n
                isUnit = True

                print("\nUnits Recorded Successfully")
                print("-" * 35)
                print(f"Units Consumed : {unit}")
            else:
                print("Invalid Units!")

        case 2:

            if isUnit:

                if unit <= 100:
                    bill = unit * 5

                elif unit <= 200:
                    bill = (100 * 5) + ((unit - 100) * 7)

                else:
                    bill = (100 * 5) + (100 * 7) + ((unit - 200) * 10)

                print("\nBILL CALCULATION")
                print("-" * 35)
                print(f"Units Consumed : {unit}")
                print(f"Bill Amount    : ₹{bill}")

            else:
                print("Please enter units consumed first.")

        case 3:

            if bill > 0:

                if bill > 2000:
                    surcharge = bill * 10 // 100
                    rate = 10
                else:
                    surcharge = bill * 5 // 100
                    rate = 5

                print("\nSURCHARGE DETAILS")
                print("-" * 35)
                print(f"Surcharge Rate : {rate}%")
                print(f"Surcharge      : ₹{surcharge}")

            else:
                print("Please calculate the bill first.")

        case 4:

            if bill > 0:

                total = bill + surcharge

                print("\n" + "=" * 45)
                print("             ELECTRICITY BILL")
                print("=" * 45)
                print(f"Units Consumed : {unit}")
                print(f"Bill Amount    : ₹{bill}")
                print(f"Surcharge      : ₹{surcharge}")
                print("-" * 45)
                print(f"Total Payable  : ₹{total}")
                print("=" * 45)

            else:
                print("Please calculate the bill first.")

        case 5:

            print("\n" + "=" * 60)
            print("     THANK YOU FOR USING ELECTRICITY BILL SYSTEM")
            print("           Program Closed Successfully")
            print("=" * 60)
            break

        case _:
            print("Invalid Choice! Please try again.")

    print("\n" + "*" * 60)
