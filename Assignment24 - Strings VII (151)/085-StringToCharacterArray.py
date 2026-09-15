'''
Convert a String into a Character Array

Write a Python program to input a string and convert it into
a character array without using any built-in conversion
functions.

Input:
Hello

Output:
['H', 'e', 'l', 'l', 'o']
'''

s = input("Enter The String : ")

arr = [0] * len(s)
# print(arr)


for i in range(len(arr)):
    arr[i]=s[i]


    

print(arr)