'''
Question:
Reverse only the vowels in a string.

Given a string, reverse the order of only the vowels
(a, e, i, o, u). All consonants, digits, spaces, and
special characters must remain at their original positions.

Test Cases:

1. Input:
   hello
   Output:
   holle

2. Input:
   hello world
   Output:
   hollo werld

3. Input:
   python
   Output:
   python

4. Input:
   education
   Output:
   noitacude

5. Input:
   apple
   Output:
   eppla

6. Input:
   aeiou
   Output:
   uoiea

7. Input:
   Hello World
   Output:
   Hollo Werld

8. Input:
   hello123!
   Output:
   holle123!

9. Input:
   xyz
   Output:
   xyz

10. Input:
    AEIOU
    Output:
    UOIEA
'''

s = input("Enter the string: ")

vow = ""

for i in s:
    if i in "AEIOUaeiou":
        vow += i

vow = vow[::-1]

new = ""
j = 0

for i in s:
    if i in "AEIOUaeiou":
        new += vow[j]
        j += 1
    else:
        new += i

print(new)

    
    

