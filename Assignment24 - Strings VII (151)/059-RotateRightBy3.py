'''
Question:
Rotate the characters of a string by 3 positions to the right.

Move the last 3 characters to the beginning of the string.
The relative order of all characters must remain unchanged.

Test Cases:

1. Input:
   hello
   Output:
   llohe

2. Input:
   abcdef
   Output:
   defabc

3. Input:
   python
   Output:
   honpyt

4. Input:
   abcde
   Output:
   cdeab

5. Input:
   abc
   Output:
   abc

6. Input:
   ab
   Output:
   ab

7. Input:
   hello123
   Output:
   123hello

8. Input:
   123456
   Output:
   456123
'''

s=input("Enter The String : ")
k=3
new=""
k=k%len(s)



for i in range(len(s)-k,len(s)):
    new+=s[i]

for i in range(len(s)-k):
    new+=s[i]


print(new)