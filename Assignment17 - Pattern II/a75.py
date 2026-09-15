'''
Docstring for a74
1 2 3 4 5 6 7 8 9 
  1 + + + + + 7
    1 + + + 5
      1 + 3
        1

'''
n=int(input("Enter the number "))

i=1

while i<=n:
    j=1
    while j<=i-1:
        print(" ",end=" ")
        j+=1

   

    if i==1:
        k=1
        while k<=2*(n-i)+1:
            print(k,end=" ")
            k+=1
    elif i == n:
        print(1, end=" ")

    else:
        print(1, end=" ")

        k = 1
        while k <= 2 * (n - i) - 1:
            print("+", end=" ")
            k += 1

        print(2 * (n - i) + 1, end=" ")


    print()
    i+=1