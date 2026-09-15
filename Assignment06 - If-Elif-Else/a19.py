'''

4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''
sub = input("Enter Subscription Type (premium/basic): ").lower()
progress = int(input("Enter Course Progress: "))
score = int(input("Enter Test Score: "))



if sub=="premium":
    if progress>=80:
        if score >=70:
            print("unlock certificate")
        else:
            print("allow retry")
    else:
        print("complete the course")
elif sub=="basic":
    if progress>=50:
        print("limited access")
    else:
        print("lock content")

else:
    print("deny access")
        