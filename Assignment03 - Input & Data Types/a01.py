'''
Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
'''
dist=int(input("Enter The Distance :- "))
time=int(input("Enter The Time :-"))
print(f"Distance {dist} km")
print(f"Time {time} hrs")
print(f"Speed = {int(dist/time)} km/h")