'''
Count How Many Times a Substring Appears in a String

Write a Python program to input a string and a substring.
Count how many times the substring appears in the string.

Overlapping occurrences should also be counted.

Input:
Enter a string: ababab
Enter a substring: aba

Output:
Occurrences: 2
'''

s = input("Enter The String : ")
sub=input("Enter The Substring : ")
count = 0
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        temp += s[j]

        
        if sub == temp:
            print(temp)
            count += 1

print(count)