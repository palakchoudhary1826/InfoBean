'''
Docstring for Assignment17(Pattern-II).a26
*
* #
* # *
* # * # 
* # * # *

'''

n=int(input("Enter The Number  : "))

i=1
while i<=n:
    j=1
    while j<=i:
        if j%2==0:
            print("#",end=" ")
        else:
            print("*",end=" ")
        j+=1
    print()
    i+=1
