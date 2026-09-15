'''
Docstring for Assignment15(Pattern).a08
654321
 65432
  6543
   654
    65
     6
'''

n=int(input("Enter The Range : "))

i=1
while i<=n:
    k=0
    while k<i:
        print(" ",end="")
        k+=1
    j=n
    while j>=i:
        print(j,end="")
        j-=1
    
    print()
    i+=1