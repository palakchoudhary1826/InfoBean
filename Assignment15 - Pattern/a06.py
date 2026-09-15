"""
Docstring for Assignment15(Pattern).a06
a
ab
abc
abcd
abcde
"""
n=int(input("Enter The Range : "))

i=1
while i<=n:
    j=0
    while j<i:
        print(chr(ord("a")+j),end="")
        j+=1
    print()
    i+=1