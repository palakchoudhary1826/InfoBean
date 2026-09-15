'''
Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12

'''

n=int(input("Enter The Num : "))
i=1
sum=0
while i<=n:
    if n%i==0:
        sum+=i
    i+=1
    
print(f"Factors Count : {sum}")