'''
Problem:

Remove Adjacent Duplicates Recursively.

Given a string s, remove adjacent duplicate characters
repeatedly until no adjacent duplicates remain.

Example 1:
Input:
s = "abbaca"

Output:
"ca"

Example 2:
Input:
s = "azxxzy"

Output:
"ay"

Example 3:
Input:
s = "aabbcc"

Output:
""

Example 4:
Input:
s = "abc"

Output:
"abc"
'''
s=input("Enter the String : ")

while True:
    found=False
    i=0
    ans=""
    while i<len(s):

        # ye first char check kar rha with second one
        if i+1<len(s) and s[i]==s[i+1]:
            ch=s[i]
            #ye duplicate ko skip kar rha hai 
            while i<len(s) and s[i]==ch:
                i+=1
            found=True
        else:
            ans+=s[i]
            i+=1
    
    s=ans

    if not found:
        break


if not s:
    print("Empty")
else:
    print(s)









