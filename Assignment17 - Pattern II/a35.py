'''
Docstring for Assignment17(Pattern-II).a35
* * * * *
* . . *
* . *
* *
*


'''

n=int(input("Enter The Number : "))

i=1

while i<=n:
    if i==1:
        j=1
        while j<=n-i+1:
            print("*",end=" ")
            j+=1
    
    elif i>1 and i<n-1:
        j=1
        print("*",end=" ")
        while j<=n-(i+1):
            print(".",end=" ")
            j+=1
        print("*",end=" ")

    else:
        j=1
        while j<=n-i+1:
            print("*",end=" ")
            j+=1
    print()
    i+=1

    