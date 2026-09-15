'''
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''
runs=int(input("Enter The Run : "))
over,ball=map(int,input("Enter the Over then balls (e.g. 48.3) : ").split("."))

totalBall = (over*6)+ball
print(f"Total Balls : {totalBall}")
rate=runs/(totalBall/6)
print(f"Run Rate : {rate:.2f}")

