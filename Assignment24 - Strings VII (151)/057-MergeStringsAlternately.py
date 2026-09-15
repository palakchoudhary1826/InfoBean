'''
Question:
Merge two strings alternatively (character by character).

Given two strings, merge them by taking one character
from the first string, then one character from the
second string, and continue until both strings are
completely merged.

If one string is longer, append its remaining characters
at the end.

Test Cases:

1. Input:
   s1 = "abc"
   s2 = "123"
   Output:
   a1b2c3

2. Input:
   s1 = "hello"
   s2 = "world"
   Output:
   hweolrllod

3. Input:
   s1 = "abc"
   s2 = "12"
   Output:
   a1b2c

4. Input:
   s1 = "ab"
   s2 = "1234"
   Output:
   a1b234

5. Input:
   s1 = "Python"
   s2 = "123"
   Output:
   P1y2t3hon

6. Input:
   s1 = ""
   s2 = "abc"
   Output:
   abc

7. Input:
   s1 = "abc"
   s2 = ""
   Output:
   abc

8. Input:
   s1 = "A"
   s2 = "1"
   Output:
   A1
'''
s1=input("Enter The String 1 : ")
s2=input("Enter The String 2 : ")
new=""
i=0
j=0
k=0

while i<len(s1) and j<len(s2):
    new+=s1[i]
    i+=1
    k+=1

    new+=s2[j]
    j+=1
    k+=1

while i<len(s1):
    new+=s1[i]
    i+=1
    k+=1

while j<len(s2):
    new+=s2[j]
    j+=1
    k+=1

    
print(new)

