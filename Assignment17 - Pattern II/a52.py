'''
Docstring for Assignment17(Pattern-II).a50
The Number : 5
The Number : 5
1 2 3 4 5 
. 1 - - 4
. . 1 - 3
. . . 1 2
. . . . 1
'''

n=int(input("The Number : "))

i=1
while i<=n:
    j=1

    while j<=i-1:
        print(".",end=" ")
        j+=1

    if i==1:
        k=1
        while k<=n-i+1:
            print(k,end=" ")
            k+=1
    elif i>=n-1:
        k=1
        while k<=n-i+1:
            print(k,end=" ")
            k+=1
    else:
        print(1,end=" ")
        k=1
        while k<=n-i-1:
            print("-",end=" ")
            k+=1
        print(n-i+1,end=" ")
   
    print()
    i+=1