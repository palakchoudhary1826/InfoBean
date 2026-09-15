'''
Find the Longest Mirror-Image Substring at Both Ends

Write a Python program to input a string and find the
longest substring at the beginning whose reverse appears
at the end.

Input:
Enter a string: abcXYZcba

Output:
Longest Mirror Substring: abc
'''
s=input("Enter The String : ")
longest=""
for i in range(1,len(s)//2+1):
    prefix=s[:i]
    suffix=s[len(s)-i:]
    

    if prefix==suffix[::-1]:
        longest=prefix
print(longest)