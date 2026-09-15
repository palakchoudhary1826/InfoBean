'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220

'''
bike=10
car=20
bus=50

vehicle=input("Enter The Type (car/bike/bus) : ").lower()
parked=int(input("Enter The Parking Time (in hrs) :"))
fee=0
if parked>5:
    if vehicle=="bike":
        fee=(parked*10)+100
    elif vehicle=="car":
        fee=(parked*20)+100
    else:
        fee=(parked*50)+100
else:
    if vehicle=="bike":
        fee=(parked*10)
    elif vehicle=="car":
        fee=(parked*20)
    else:
        fee=(parked*50)
        
print(f"Total Parking Fee: {fee}")
    
        
    
