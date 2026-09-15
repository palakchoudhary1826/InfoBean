'''

Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''

dist=int(input("Enter The Distance : "))
mileage=int(input("Enter the Mileage : "))
price =int(input("Enter The Price : "))

print(f"Distance :{dist} km \nMileage : {mileage} km/litre\nPetrol Price :{price}")
print(f"cost : {(dist/mileage)*price}")