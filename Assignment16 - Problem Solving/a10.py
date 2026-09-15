'''
Docstring for Assignment16.a10
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
'''

n = int(input("Enter the Number of Houses: "))

bill = 0
total = 0
high = 0

i = 1
while i <= n:
    print(f"\nHouse No. {i}")

    unit = int(input("Enter the Units: "))

    if unit < 100:
        if unit < 50:
            bill -= 100
        bill += unit * 5

    elif unit <200:
        bill = (100 * 5) + (unit - 100) * 7

    else:
        bill = (100 * 5) + (100 * 7) + (unit - 200) * 10

    if bill > 2000:
        surcharge = (bill * 10) // 100
        bill += surcharge

    print(f"House {i} Bill: {bill}")

    total += bill

    if bill > high:
        high = bill

    bill = 0
    i += 1

print("\n------ Electricity Bill Summary ------")
print(f"Total Collection : {total}")
print(f"Highest Bill     : {high}")
