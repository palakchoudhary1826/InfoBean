'''
Print All Permutations of a String Without Repetition

Write a Python program to input a string and print all possible
permutations of the string without repetition.

Input:
ABC

Output:
ABC
ACB
BAC
BCA
CAB
CBA
'''

def permutations(s):
    used = [False] * len(s)  
    current = []

    backtrack(s,used, current)


def backtrack(s, used,current):

    # Base case -> stop ABC
    if len(current) == len(s):
        print("".join(current))
        return

   # recursive case -> leap of faith 
    # Try every character
    for i in range(len(s)):

        if used[i]:
            continue

        # Choose ->A
        used[i] = True
        current.append(s[i])

        # Explore -> A -> AB -> ABC
        backtrack(s,used, current)

        # Undo / Backtrack  ABC -> AB ->A 
        current.pop()
        used[i] = False


permutations("abc")
