'''

Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
'''

d1=int(input("Enter The Distance1 : "))
t1=int(input("Enter The Time1 : "))
d2=int(input("Enter The Distance2 : "))
t2=int(input("Enter The Time1 : "))

avgSpd=(d1+d2)/(t1+t2)

print(f"Average Speed :{avgSpd} km/h")