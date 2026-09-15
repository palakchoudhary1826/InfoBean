'''
11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600

'''

d=int(input("Enter The Distance : "))
c=input("Enter The Class (ac/sleeper) : ").lower()
f=0

if d<=100:
    if c=="ac":
        f=100
    else:
        f=200

elif d<=500:
    if c=="ac":
        f=600
    else:
        f=300
        
else:
    if c=="ac":
        f=1000
    else:
        f=500
        
print(f"total fare : {f}")
        