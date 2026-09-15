
'''
Question:
Rotate the characters of a string by 2 positions to the left.

Move the first 2 characters to the end of the string.
The relative order of all characters must remain unchanged.

Test Cases:

1. Input:
   hello
   Output:
   llohe

2. Input:
   abcdef
   Output:
   cdefab

3. Input:
   python
   Output:
   thonpy

4. Input:
   abc
   Output:
   cab

5. Input:
   ab
   Output:
   ab

6. Input:
   a
   Output:
   a

7. Input:
   hello123
   Output:
   llo123he

8. Input:
   123456
   Output:
   345612
'''
s=input("Enter The String : ")
k=2
new=""
k=k%len(s)




for i in range(k,len(s)):
    new+=s[i]

for i in range(k):
    new+=s[i]

print(new)