'''
Docstring for a10
Question 10: Lift Mode Operation – Smart Elevator System

Write a program to:

- If mode = 1:
  Read current and destination floor.
  Print all floors in ascending order.

- If mode = 2:
  Read current and destination floor.
  Print all floors in descending order.

- If mode = 3:
  Read destination floor.
  Print alternate floors from 0 to destination.

- Otherwise:
  Print "Emergency Alarm" 4 times using a loop.

Input

3
6

Output

0 2 4 6
'''
mode=int(input("Enter The Mode (1 or 2 or 3): "))

if mode==1:
    curr=int(input("Enter The Current Floor : "))
    dest=int(input("Enter The Destination Floor : "))
    while curr<=dest:
        print(curr,end=" ")
        curr+=1


elif mode==2:
    curr=int(input("Enter The Current Floor : "))
    dest=int(input("Enter The Destination Floor : "))
    while dest>=curr:
        print(dest,end=" ")
        dest-=1

elif mode==3:
    dest=int(input("Enter The Destination Floor : "))
    i=0
    while i<=dest:
        print(i,end=" ")
        i+=2

else:
    for i in range(0,4):
        print("Emergency Alarm !!!!🪦")

