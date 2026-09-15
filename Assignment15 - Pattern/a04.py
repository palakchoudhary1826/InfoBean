"""
Docstring for Assignment15(Pattern).a04
1
00
111
0000
11111
"""

n=int(input("Enter The Range : "))

i=1
while i<=n:
    j=1
    while j<=i:
        if i%2==0:
            print(1,end="")
        else:
            print(0,end="")
        j+=1
    print()
    i+=1