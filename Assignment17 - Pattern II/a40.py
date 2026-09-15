'''
Docstring for Assignment17(Pattern-II).a40
*
**
****
*******
***********

'''
n=int(input("The Number :"))
s=1
i=1
while i<=n:

    j=1
    while j<=s:
        print('⭐',end=" ")
        j+=1
    s+=i
    print()
    i+=1