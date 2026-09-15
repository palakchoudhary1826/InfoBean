'''
1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250 100->101

Output:
Total Electricity Bill: ₹1950

'''

unit=int(input("Enter The Unit : "))
charge=0

'''

if unit>=100:
    charge+=(100*5)
    unit-=100
   
unit1=unit
if unit1>=100:
    charge+=(100*7)
    unit1-=100
    
unit2=unit1

if unit2>=100 or unit2<=100:
    charge+=(unit2*10)
 '''

if unit <= 100:
    print(f"charge : {unit * 5}")

elif unit <= 200:
    print(f"charge : {(100 * 5) + ((unit - 100) * 7)}")

else:
    print(f"charge : {(100 * 5) + (100 * 7) + ((unit - 200) * 10)}")


        