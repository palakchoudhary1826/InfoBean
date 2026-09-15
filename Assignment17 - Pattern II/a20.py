'''
Docstring for Assignment17(Pattern-II).a20
1
1 2
1 . 3
1 . . 4
1 2 3 4 5

'''

n=int(input("Enter the Number : "))

i=1
while i<=n:
    if i<=2:
        j=1
        while j<=i:
            print(j,end=" ")
            j+=1
        
    elif i==n:
        j=1
        while j<=n:
            print(j,end=" ")
            j+=1

        
    else:
        j=1
        print(1,end=" ")
        while j<=i-2:
            print(".",end=" ")
            j+=1
        print(i,end=" ")

    print()
    
    i+=1
