'''
Docstring for Assignment17(Pattern-II).a61
The Number : 5

        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
'''
n=int(input("The Number : "))

i=1
while i<=n:

    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    k=1
    while k<=2*i-1:
        print(k,end=" ")
        k+=1
    

    print()
    i+=1