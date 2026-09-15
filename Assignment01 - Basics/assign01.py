'''Ques-1
1. Hello & Name Printer
Write a program to print:
Hello
Your Name
'''

'''Solution
name="abhiraj"
print("hello ",name)
'''

'''Ques-2
2. Menu Display
Write a program to display:
=== Welcome to Coffee Shop ===
1. Espresso     $3
2. Latte        $4
3. Cappuccino   $5
==============================
'''

'''Solution
print(3*"=" , end=" ")
print("Welcome to Coffee Shop",end=" ")
print(3*"=")
print("1. Espresso\t$3")
print("2. Latte\t$4")
print("3. Cappuccino\t$5")
print(30*"=")
'''

'''Ques-3
3. Resume Format
Write a program to display:
=== Resume ===
Name       : Alice Johnson
Email      : alice@example.com
Skills     :
  - Java
  - HTML & CSS
  - Problem Solving
Experience : 2 years at XYZ Ltd.
'''

'''Solution
name="Abhiraj Jaiswal"
email="abhi@gmail.com"
exp="2 years at XYZ ltd."
print(3*"=" ,end=" ")
print("Resume",end=" ===")
print("\nName\t:",name)
print("Email\t:",email)
print("Skills\t: -Java\n\t  -HTML & CSS\n\t  -Problem Solving")
print("Experience:",exp)
'''

'''Ques-4
4. Star Pattern(without loop)
Write a program to print:
***
***
***
'''

'''Solution
print(3*"*")
print(3*"*")
print(3*"*")
'''

'''Ques-5
5. Special Characters
Write a program to print:
@ # $ % ^ & *
'''

'''Solution
print("@ # $ % ^ & *")
'''

'''Ques-6
6. Print User Details
Take input:
- Name
- Age
- City
Display them properly.
'''

'''Solution
name=input("Enter Your Name : ")
age=input("Enter Your Age : ")
city=input("Enter Your City Name : ")
print("Name\t:",name)
print("Age\t:",age)
print("City\t:",city)
'''

'''Ques-7
7. Full Name Display
Take first name and last name as input and display:
Full Name: John Doe
'''

'''Solution
Fname=input("Enter Your First Name : ")
Lname=input("Enter Your Last Name  : ")
print(f"{Fname} {Lname}")
'''

'''Ques-8
8. Simple Input Display
Take two numbers as input and print them on separate lines
'''

'''Solution
a,b=input("Enter the Two Numbers :").split()
print(a+"\n"+b)
'''

'''Ques-9
9. Three Inputs Display
Take three values from user and print each on new line.
'''

'''Solution
a,b,c=input("Enter the Three Numbers :").split()
print(a+"\n"+b+"\n"+c)
'''

'''Ques-10
10. Input and Echo
Take input from user and print:
You entered: <input>
'''

'''Solution
enter=input("Enter the song name :")
print("Your enter song name :",enter)
'''

'''Ques-11
11. Greeting Message
Take name as input and print:
Hello <name>
Welcome to Python
'''

'''Solution
name=input("Enter Your Name : ")
print(f"Hello {name}\nWelcome to Python")
'''


'''Ques-12
12. Favorite Things
Take input:
- Favorite food
- Favorite color
Display:
I like <food> and my favorite color is <color>
'''

'''solution
food=input("Enter Your Fav Food : ")
color=input("Enter Your Fav Color : ")
print(f"I like {food} and my favorite color is {color}")
'''

'''Ques-13
13. College Details
Take input:
- College Name
- Course
- Year
Display in proper format.
'''

'''solution
clgName=input("Enter Your College Name : ")
course=input("Enter Enrolled Course : ")
yr=input("Enter Year : ")

print("College \t:",clgName)
print("Course \t:",course)
print("Year \t:",yr)
'''

'''Ques-14
14. Email Display
Take email as input and print:
Your email is: <email>
'''

'''Solution
email=input("Enter the Email : ")
print(f"your email is {email}")
''' 


'''Ques-15
15. Bio Data
Take input:
- Name
- Age
- Phone
Display:
--- Bio Data ---
Name  :
Age   :
Phone :
'''

'''Solution
name=input("enter the name : ")
age=input("enter the age : ")
phone=input("enter the phone : ")

print(3*"=",end=" ")
print("Bio Data",end="===")
print("\nname\t:",name)
print("phone\t:",phone)
print("age\t:",age)
'''