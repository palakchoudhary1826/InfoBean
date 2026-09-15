'''
Docstring for Assignment17(Pattern-II).a47
         X  
       X   X
     X   _   X
   X   _   _   X
 X   X   X   X   X

'''

n=int(input("The Number : "))

i=1
while i<=n:

    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    if i<=2:
        k=1
        while k<=i:
            print(" X ",end=" ")
            k+=1
    elif i==n:
        l=1
        while l<=n:
            print(" X ",end=" ")
            l+=1
               
    else:
        print(" X ",end=" ")
        l=1
        while l<=i-2:
            print(" _ ",end=" ")
            l+=1
        print(" X ",end=" ")

    print()
    i+=1

