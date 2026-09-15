"""
Docstring for a88
        1
        2
        3
        4
1 2 3 4 5 4 3 2 1 
        4
        3
        2
        1
"""
n=int(input("enter the num : "))
k=n-1
m=n-1

i=1
while i<=n*2-1:
    j=1
    while j<=n*2-1:
        
        
        if i == n and j <= n:
            print(j, end=" ")

        elif i == n and j > n:
            print(2 * n - j, end=" ")

        elif j == n:
            if i <= n:
                print(i, end=" ")
            else:
                print(2 * n - i, end=" ")

        else:
            print(" ", end=" ")
        
        j+=1
    print()
    i+=1

