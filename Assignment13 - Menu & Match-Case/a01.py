'''
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions

'''

while True :
    print(f"1 -> Check Prime Number ")
    print(f"2 -> Check Palindrome Number ")
    print(f"3 -> Reverse A Number ")
    print(f"4 -> Count Digits ") 
    print(f"5 -> Exit ")
    print("")
    print("*"*20)
    print("")

    choice =int(input("Enter Your Choice: "))

    match choice:
        case 1:
            print("Check Prime Number")
            n=int(input("Enter The Number: "))
            if n<=1:
                print("Not Prime")
            else:
                i=2
                while i*i<=n:
                    if n%i==0:
                        print("Not Prime")
                        break
                    i+=1
                else:
                    print("Prime ")

        case 2:
            print("Check Palindrome Number")
            n=int(input("Enter The Number: "))
            rev=0
            while n>0:
                d=n%10
                rev=rev*10+d
                n//=10
            if n==rev:
                print("Palindrome")
            else:
                print("Not Palindrome")

        case 3:
            print("Reverse A Number")
            n=int(input("Enter The Number: "))
            n1=n
            rev=0
            while n>0:
                d=n%10
                rev=rev*10+d
                n//=10
            print(f"Reverse of {n1}: {rev}")
        
        case 4:
            print("Count Digits")
            n=int(input("Enter The Number: "))
            n1=n
            count=0
            while n>0:
                count+=1
                n//=10
            print(f"Number of Digit in {n1} : {count}")

        case 5:
            print("Exiting ....")
            break
    print("")
    print("*"*20)