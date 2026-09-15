'''
Docstring for Assignment17(Pattern-II).a57
    *
   * *
  * * *
 * * * *
* * * * *

'''
n=int(input("The Number : "))

i=1
while i<=n:

    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    k=1
    while k<=i:
        print(" * ",end=" ")
        k+=1
    print()
    i+=1
