'''
Docstring for Assignment17(Pattern-II).a57
             A 
            A   B
          A   B   C
        A   B   C   D
      A   B   C   D   E

'''
n=int(input("The Number : "))

i=0
while i<n:

    j=0
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    k=0
    while k<=i:
        print(" ",chr(ord('A')+k),end=" ")
        k+=1
    print()
    i+=1
