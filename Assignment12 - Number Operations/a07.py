'''
Docstring for a07
Question 7: Alternate Digit Prime Checker

Write a program to:

Find the sum of alternate digits from the right side.
Check whether the sum is Prime or Not Prime.

Input

12345

Output

Alternate Sum = 9
Not Prime
'''
n=int(input("Enter the Number : "))

l=len(str(n))
sum=0

# if l%2==0:
#     for i in range(l,0,-1):
        
#         if i%2==0:
#             d=n%10
#             # print(d)
#             sum+=d
#             n//=100
# else:
#     for i in range(l,0,-1):
#         if i%2!=0:
#             d=n%10
#             # print(d)
#             sum+=d
#             n//=100

for i in range(l,0,-1):
    d=n%10
    print(d)
    sum+=d
    n//=100

print(sum)



if sum<=1:
    print("not prime")
else:
    i=2
    while i*i<=sum:
        if sum%i==0:
            print("not prime")
            break
        i+=1
    else:
        print("prime")

