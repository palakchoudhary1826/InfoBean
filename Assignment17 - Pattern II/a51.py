'''
Docstring for Assignment17(Pattern-II).a51
The Number : 5
5 5 5 5 5 
. 4 4 4 4
. . 3 3 3
. . . 2 2
. . . . 1
'''

n=int(input("The Number : "))

i=1
while i<=n:
    j=1

    while j<=i-1:
        print(".",end=" ")
        j+=1
    k=1
    while k<=n-i+1:
        print(n-i+1,end=" ")
        k+=1
    
   
    print()
    i+=1