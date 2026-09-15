'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''
p=5000
d=4000
m=3000

s=input("Enter The Course Category (programming/marketing/design) : ").lower()
t=input("Enter The User Type (student/working/others) : ").lower()
discount=0;
if s=="programming":
    if t=="student":
        discount=(p*20)/100
    elif t=="working":
        discount=(p*10)/100
    else:
        print("no discount")
elif s=="marketing":
    if t=="student":
        discount=(m*20)/100
    elif t=="working":
        discount=(m*10)/100
    else:
        print("no discount")

else:
    if t=="student":
        discount=(d*20)/100
    elif t=="working":
        discount=(d*10)/100
    else:
        print("no discount")
        
        
print(discount)