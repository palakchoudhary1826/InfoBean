"""
Docstring for Assignment15(Pattern).a02
WAP to print sq , cube and square root of all number from 1 to N 
"""
import math
n=int(input("Enter The Value of N: "))
i=1
while i<=n:
    print(F"Number: {i}")
    print(f"Square  : {i**2}")
    print(f"Cube    : {i**3}")
    print(f"Sq Root : {math.sqrt(i):.2f}")
    print("-"*30)
    i+=1
