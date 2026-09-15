"""
Docstring for Assignment15(Pattern).a03
WAP to find out all the leap years between two entered years
"""
a=int(input("Enter The First Year: "))
b=int(input("Enter The Second Year: "))


while a<=b:
    d=a%100
    if d==00:
        if a%400==0 and a%100==0 and a%4==0:
            print(a)
    else:
        if a%4==0:
            print(a)
    a+=1