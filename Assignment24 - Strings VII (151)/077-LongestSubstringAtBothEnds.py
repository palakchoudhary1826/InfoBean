'''
Find the Longest Substring That Appears at Both Ends

Write a Python program to input a string and find the
longest substring that appears at both the beginning and
the end of the string.

The prefix and suffix must not overlap.

Input:
Enter a string: abcXYZabc -> 9/2-> 5

Output:
Longest Substring: abc
'''

s = input("Enter The String : ")

longest = ""

for i in range(1, len(s)//2 + 1):

    prefix = s[:i]
    suffix = s[len(s)-i:]

    if prefix == suffix:
        longest = prefix


if longest:
    print(longest)
else:
    print("not found")
