'''
Docstring for Assignment17(Pattern-II).a19
*
* *
* . *
* . . *
* * * * *


'''
n=int(input("Enter the Number : "))

i=1
while i<=n:
    if i<=2:
        j=1
        while j<=i:
            print('*',end=" ")
            j+=1
        
    elif i==n:
        j=1
        while j<=n:
            print('*',end=" ")
            j+=1

        
    else:
        j=1
        print("*",end=" ")
        while j<=i-2:
            print(" ",end=" ")
            j+=1
        print("*",end=" ")

    print()
    
    i+=1


