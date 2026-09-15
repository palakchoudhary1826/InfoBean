'''
Docstring for Assignment17(Pattern-II).a21
1
2 2
3 . 3
4 . . 4
5 5 5 5 5
'''
n=int(input("Enter the Number : "))

i=1
while i<=n:
    if i<=2:
        j=1
        while j<=i:
            print(i,end=" ")
            j+=1
        
    elif i==n:
        j=1
        while j<=n:
            print(i,end=" ")
            j+=1

        
    else:
        j=1
        print(i,end=" ")
        while j<=i-2:
            print(".",end=" ")
            j+=1
        print(i,end=" ")

    print()
    
    i+=1
