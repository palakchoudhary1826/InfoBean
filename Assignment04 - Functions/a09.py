'''
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0

'''

d=int(input("Enter The Distance : "))
m=int(input("Enter The Mileage : "))
p=int(input("Enter The Petril Price : "))
use=d/m
print(f"Petrol Used :{use} litres")
print(f"Total Cost : {use*p}")