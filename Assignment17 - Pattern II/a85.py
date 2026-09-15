'''
Docstring for a85
Enter the N :5
*         *
**       **
***     ***
****   ****
***** *****
'''
n=int(input("Enter the N :"))
i = 1
star = 1
space = 2 * n - 1

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

    star += 1
    space -= 2
    i += 1