"""
Docstring for Assignment15(Pattern).a10
0
01
012
0123
01234
"""

n=int(input("Enter The Range : "))

i=1
while i<=n:
    j=0
    while j<i:
        print(j,end="")
        j+=1
    print()
    i+=1