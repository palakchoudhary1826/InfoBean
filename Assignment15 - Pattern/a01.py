"""
Docstring for Assignment15(Pattern).a01
WAP find out the sum of all integer between 100 and 200 which are divisible by 9
"""

a=int(input("Enter The 1st Num : "))
b=int(input("Enter The 2nd Num : "))

sum=0

while a<=b:
    if a%9==0:
        sum+=a
    a+=1

print(sum)