'''
Docstring for a02
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
'''

n=int(input("Enter The Number : "))
m=n+1
flag=True
ans=0

while m<(n*2):
    i=2
    while i*i<=m:
        if m%i==0:
            flag=False
            break
        i+=1
    if flag:
        ans=m
        break
    else:
        flag=True
        m+=1

print(f"next prime : {ans}")

    
            
