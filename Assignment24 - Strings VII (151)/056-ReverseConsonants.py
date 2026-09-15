'''
Question:
Reverse only the consonants in a string.

Given a string, reverse the order of only the consonants.
Vowels, digits, spaces, and special characters must remain
at their original positions.

Consonants:
All English alphabet characters except a, e, i, o, u.

Test Cases:

1. Input:
   hello
   Output:
   leloh

2. Input:
   hello world
   Output:
   wollo hreld

3. Input:
   python
   Output:
   nohtyp

4. Input:
   education
   Output:
   nducation

5. Input:
   apple
   Output:
   elppa

6. Input:
   abcde
   Output:
   edcba

7. Input:
   Hello World
   Output:
   Dello WorlH

8. Input:
   hello123!
   Output:
   leloh123!

9. Input:
   aeiou
   Output:
   aeiou

10. Input:
    xyz
    Output:
    zyx
'''

s=input("Enter The String : ")
con = ""

for i in s:
    if i not in "AEIOUaeiou":
        con += i

con = con[::-1]

new = ""
j = 0

for i in s:
    if i not in"AEIOUaeiou":
        new += con[j]
        j += 1
    else:
        new += i

print(new)
