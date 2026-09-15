'''
Docstring for Assignment17(Pattern-II).a47
. . . . 1 
. . . 1 0
. . 1 0 1
. 1 0 1 0
1 0 1 0 1

'''

n=int(input("The Number : "))

i=1
while i<=n:

    
    j=1
    while j<=n-i:
        print(".",end=" ")
        j+=1

    k=1
    while k<=i:
        if k%2!=0:
            print(1,end=" ")
        else:
            print(0,end=" ")
        k+=1
    

    print()
    i+=1

