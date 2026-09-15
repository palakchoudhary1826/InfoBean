"""
Docstring for Assignment15(Pattern).a05
A
AB
ABC
ABCD
ABCDE
"""
n=int(input("Enter The Range : "))

i=1
while i<=n:
    j=0
    while j<i:
        print(chr(ord("A")+j),end="")
        j+=1
    print()
    i+=1
# print(chr(ord("A")+4))