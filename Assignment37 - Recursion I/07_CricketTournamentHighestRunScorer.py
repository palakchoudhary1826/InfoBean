'''
Question 7: Cricket Tournament – Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Task:
Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input:
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]

Expected Output:
Highest Run Scorer: Rohit
'''

from functools import reduce

def high(x,y):
    if x[1]>y[1]:
        return x
    return y

players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]

ans=reduce(high,players)
print(ans[0])