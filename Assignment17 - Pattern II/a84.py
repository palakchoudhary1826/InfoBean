'''
Docstring for a84
Enter n: 5
***** *****
****   ****
***     ***
**       **
*         *
'''


n = int(input("Enter n: "))

# Upper half
i = 1
star = n
space = 1

while i <= n:
    j = 1
    while j <= star:
        print("*", end="")
        j += 1

    j = 1
    while j <= space:
        print(" ", end="")
        j += 1

    j = 1
    while j <= star:
        print("*", end="")
        j += 1

    print()

    star -= 1
    space += 2
    i += 1