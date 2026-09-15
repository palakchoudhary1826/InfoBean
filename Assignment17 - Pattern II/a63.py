'''
Docstring for Assignment17(Pattern-II).a61
The Number : 5

            A 
          A B C
        A B C D E
      A B C D E F G
    A B C D E F G H I
'''
n=int(input("The Number : "))

i=0
while i<n:

    j=0
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    k=0
    while k<2*i+1:
        print(chr(ord('A')+k),end=" ")
        k+=1
    

    print()
    i+=1