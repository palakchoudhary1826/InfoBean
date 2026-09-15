'''
Docstring for a05
Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3
'''
n=int(input("Enter The Number : "))
count=n+1
flag=True
ans=0

while count<(n*2):
    i=2
    while i*i<=count:
        if count%i==0:
            flag=False
            break
        i+=1
    if flag:
        ans=count
        break
    else:
        flag=True
        count+=1

print(f"next prime id: {ans}")
print(f"Gap : {ans-n}")