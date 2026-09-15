'''
Docstring for Assignment15(Pattern).a09
    1
   10
  101 
 1010
10101
'''


n=int(input("Enter The Range : "))

i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=i:
        if j%2==0:
            print(0,end="")
        else:
            print(1,end="")
        j+=1
    print()
    i+=1