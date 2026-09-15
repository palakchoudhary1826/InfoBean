'''
Docstring for Assignment18.a07
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''
n=input("Enter Vehicle Number : ").lower()
# print(len(n))
# print(n.count(" "))
# print( n[:2], n[2:4],n[4:6],n[6:])
# if  n.count(" ")==0 and len(n)==10:
#     a=n[:2]
#     b=n[2:4]
#     c=n[4:6]
#     d=n[6:]
    
#     if  a.isalpha() and c.isalpha and b.isdigit() and d.isdigit():
#         print(" valid")
    
#     else:
#         print("not valid")
# else:
#     print("Not valid  ")

if len(n)==10 and " " not in n:
    
          
        if ('a' <= n[0] <= 'z' and
            'a' <= n[1] <= 'z' and
            '0' <= n[2] <= '9' and
            '0' <= n[3] <= '9' and
            'a' <= n[4] <= 'z' and
            'a' <= n[5] <= 'z' and
            '0' <= n[6] <= '9' and
            '0' <= n[7] <= '9' and
            '0' <= n[8] <= '9' and
            '0' <= n[9] <= '9' ):
            print("Valid")
        else:
            print("Invalid")
            
else:
    print("invalid")




