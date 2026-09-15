'''
Docstring for Assignment17(Pattern-II).a24
*
* *
* @ *
* @ @ *
* * * * *
'''

n=int(input("Enter the Number : "))

i=0
while i<n:
    if i<2:
        j=0
        while j<=i:
            print("*",end=" ")
            j+=1
        
    elif i==n-1:
        j=0
        while j<n:
            print("*",end=" ")
            j+=1

        
    else:
        j=0
        print("*",end=" ")
        while j<=i-2:
            print("@",end=" ")
            j+=1
        print("*",end=" ")

    print()
    
    i+=1