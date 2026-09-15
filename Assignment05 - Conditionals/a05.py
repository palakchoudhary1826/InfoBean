'''
5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password

'''

userName=input("Enter The UserName : ").lower()
password=input("Enter The Password : ")

if userName=="admin":
    print("valid user")
    if len(password)>=8:
        print("Strong Password")