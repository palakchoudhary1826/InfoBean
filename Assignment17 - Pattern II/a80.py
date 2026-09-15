'''
Docstring for a80
Enter The Number : 4
       *  

     *   *
       -
   *   *   *
     -   -
 *   *   *   *
   -   -   -
   *   *   *
     -   -
     *   *
       -
       *
'''

n = int(input("Enter The Number : "))

i = 1
c = 1
d = n - 1
e = n 
f = 0
while i <= n + (n - 1):

    if i % 2 == 0:
        k = 1

        while k <= e:

            print(" ", end=" ")
            k += 1
        e -= 1

        j = 1
        while j <= f:
            print(" - ", end=" ")
            j += 1
        f += 1

    else:
        k = 1
        while k <= d:
            print(" ", end=" ")
            k += 1
        d -= 1
        j = 1

        while j <= c:
            print(" * ", end=" ")
            j += 1
            
        c += 1
    print()
    i += 1

j=1
d=1
c=n-1
e=1

f=n-1

while j <= n + (n - 2):

    if j % 2 == 0:
        k = 1

        while k <= d:

            print(" ", end=" ")
            k += 1
        d += 1

        l = 1
        while l <= c:
            print(" * ", end=" ")
            l += 1
        c -= 1

    else:
        k = 1
        while k <= e:
            print(" ", end=" ")
            k += 1
        e += 1
        l= 1

        while l <= f:
            print(" - ", end=" ")
            l += 1
        f-= 1
    print()
    j+= 1
