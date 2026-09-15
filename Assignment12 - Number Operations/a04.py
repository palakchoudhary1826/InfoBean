'''

Docstring for a04
Question 4: Unique Digit Security Scanner

Write a program using a for-else loop to:

Check whether all digits are unique.
If any digit is repeated, print Invalid Code.
Otherwise, print Valid Unique Code.

Input

57294

Output

Valid Unique Code
'''

n = int(input("Enter The Number : "))
l = len(str(n))


# for i in range(l):
#     d1=n%10
#     temp=n//10
#     while temp>0:
#         d2=temp%10

#         if d1==d2:
#             print("invalid")
#             break
#         temp//=10
#     else:
#         n//=10
#         continue
#     break
# else:
#     print("valid")

for i in range(l):
    d1=n%10
    temp=n//10
    for j in range(l):
        
        d2=temp%10
        if d1==d2:
            print("invalid")
            break
        temp//=10
        
    else:
        n//=10
        continue
    break
else:
    print("valid")


#logic with string

        
    
        

