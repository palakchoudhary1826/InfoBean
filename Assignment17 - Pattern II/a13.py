'''
Docstring for Assignment17(Pattern-II).a13
1 
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

n=int(input("Enter The Number : "))

i=0

while i<n:
    
    if i%2==0:
        print(1,end=" ")
        j=1
        while j<=i:
       
            if j%2==0:
                print(1,end=" ")
            else:
                print(0,end=" ")
            j+=1
    else:
        print(0,end=" ")
        j=1
        while j<=i:
            if j%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
            j+=1
    print()
    i+=1