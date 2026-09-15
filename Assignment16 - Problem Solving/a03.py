'''
Docstring for Assignment16.a03
Fibonacci Population Growth Tracker

Write a program to:

Input n (number of months).
Generate the Fibonacci series up to n months.
Print the population series.
Print:
Total Population
Months with Population > 5

Input

8

Output

Population Growth:
0 1 1 2 3 5 8 13

Total Population = 33
Months with Population > 5 = 2
'''
n=int(input("Enter The Number : "))

f=0
s=1
sum=0
month=0
total=0

print("Population Growth : ")
if n>=1:
    print(f,end=" ")
    total+=f
if n>=2:
    print(s,end=" ")
    total+=s

i=0
while i<=n-3:
    sum=f+s
    total+=sum
    f=s
    s=sum
    if sum>5:
        month+=1
    print(sum,end=" ")
    
    i+=1
print()
print(f"Total Population : {total}")
print(f"Months With Population > 5 :{month}")
