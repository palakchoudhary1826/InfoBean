'''
Problem 6: Add Binary

Given two binary strings a and b, return their sum as a binary
string.

Example 1:
Input:
a = "11"
b = "1"

Output:
"100"

Explanation:
11 + 1 = 100 in binary.

Example 2:
Input:
a = "1010"
b = "1011"

Output:
"10101"

Explanation:
1010 + 1011 = 10101 in binary.

Constraints:
- 1 <= a.length, b.length <= 10^4
- a and b consist only of '0' or '1'.
- Each string does not contain leading zeros except for "0".
'''

s1=input("Enter The 1st Binary : ")
s2=input("Enter The 2nd Binary  : ")

#1+1 -> sum=0 carry=1
#0+1 -> sum=1 
#1+0 -> sum=1  carry=1
#0+0 -> sum=0

i=1
j=1
carry=0
ans=''
while i<=len(s1) or j<=len(s2) or carry!=0:
    #yha error nhi ay toh if else lgya

    if i<=len(s1):
        a=int(s1[-i]) #"1010" -> 0 
    else:
        a=0


    if j<=len(s2):
        b=int(s2[-j]) #'1011" -> 1
    else:
        b=0
       

    sum=a+b+carry # 0+1+0 -> 1
    # print(sum)
    ans+=str(sum%2) #1%2 -> 1  #2%2==0
    carry=sum//2    #1//2 -> 1 

    i+=1
    j+=1




print(ans)