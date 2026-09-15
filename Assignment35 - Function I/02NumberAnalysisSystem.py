def display():
    print("\n" + "*" * 35)
    print("      NUMBER ANALYSIS SYSTEM")
    print("*" * 35)

    print("""
1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit
""")

def perfectNumber(n):
    sum = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum += i

    return sum == n

def primeNumber(n):
    if 2 > n:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

def reverse(n):
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n//=10

    return rev

def factorial(n):
    p=1
    i=1
    while i<=n:
        p*=i
        i+=1 
    return p

def displayFactor(n):
    fact=[]
    i=1
    while i<=n:
        if n%i==0:
            fact.append(i)
        i+=1
    return fact
while True:

    display()

    choice = int(input("Enter Choice : "))

    match choice:

        case 1:
            print("Check Perfect Number ")
            n = int(input("Enter The Number :  "))
            print(perfectNumber(n))

        case 2:
            print("Check Prime Number ")
            n = int(input("Enter The Number :  "))
            print(primeNumber(n))

        case 3:
            print("Reverse The Number ")
            n = int(input("Enter The Number : "))
            result=reverse(n)

            if len(str(result))==1:
                print(f"You Entered Single Digit :{n}")
            else:
                print(f"Reverse Of Number :{result}")

        case 4:
            print("Factorial The Number ")
            n = int(input("Enter The Number : "))
            print(f"factorial Is : {factorial(n)}")

        case 5:
            print("Factor Of  Number ")
            n = int(input("Enter The Number : "))
            result=displayFactor(n)
            print(f"Factor Are : {displayFactor(n)}")

        case 6:
            print("Exiting Number Analysis System...")
            break

        case _:
            print("Invalid Choice!")
