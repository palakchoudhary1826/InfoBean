from utils.operation import *

while True:
    display()
    choice=int(input("Enter The Choice : "))
    print()

    match choice:
        case 1:
            print("Check Perfect Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(perfect_num(n))

        case 2:
            print("Check Palindrome Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(palindrome_num(n))
        case 3:
            print("Check Strong Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(Strong_num(n))
        case 4:
            print("Check Armstrong Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(armstrong_num(n))
        case 5:
            print("Check Prime Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(prime_num(n))
        case 6:
            print("Check Even or Odd Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(check_even_odd(n))
        case 7:
            print("Check factorial Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(f"factorial of {n} is {factorial(n)}")
            
        case 8:
            print("Sum Of Digit Of Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(f"Sum of digit of {n} is {sum_of_digit(n,0)}")
        case 9:
            print("Reverse Of Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(f"Reverse {n} is {reverse_num(n,0)}")
        case 10:
            print("Count Digit Of Number")
            print()
            n=int(input("Enter Number :"))
            print()
            print(f"Count digit Of  {n} is {count_num(n,0)}")
            
        case 11:
            print("Check Automorphic Number")
            print()
            n = int(input("Enter Number : "))
            print()
            print(automorphic(n))
        case 12:
            print("Check Neon Number")
            print()
            n = int(input("Enter Number : "))
            print()
            neon_num(n)
        case 13:
            print("Check Spy Number")
            print()
            n=int(input("Enter Number :"))
            print()
            spy_num(n)
        case 14:
            print("Check Harshad  Number")
            print()
            n=int(input("Enter Number :"))
            print()
            harsh_num(n)
        case 15:
            print("Thanks For Using")
            print("Exit")
        case _:
            print("Invalid Choice")
