'''
Docstring for Assignment17(Pattern-II).a27
1
1 0
1 . 1
1 . . 0
1 0 1 0 1

'''

n=int(input("Enter the Number : "))

i=1
while i<=n:
    if i<=2:
        j=1
        while j<=i:
            if j%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
            j+=1
        
    elif i==n:
        j=1
        while j<=n:
            if j%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
            j+=1

        
    else:
        j=1
        print(1,end=" ")
        while j<=i-2:
            print(".",end=" ")
            j+=1
        if i%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")

    print()
    
    i+=1
