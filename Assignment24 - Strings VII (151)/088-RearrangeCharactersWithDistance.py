'''
Problem:
Rearrange a string so that all identical characters are at least d
distance apart.

Given a string s and an integer d, rearrange the characters of s so
that any two identical characters are at least d positions apart.

If such a rearrangement is possible, return any valid rearranged string.
Otherwise, return an empty string.

Example:
Input:
s = "aabbcc"
d = 3

Output:
"abcabc"
'''

def rearrange(s, d):

    used = [False] * len(s)
    current = []

    return backtrack(s, d, used, current)


def backtrack(s, d, used, current):

    if len(current) == len(s):
        return "".join(current)

    for i in range(len(s)):

        if used[i]:
            continue

        if s[i] in current:
            last_index = current.index(s[i])

            if len(current) - last_index < d:
                continue

        used[i] = True
        current.append(s[i])

        ans = backtrack(s, d, used, current)

        if ans:
            return ans

        current.pop()
        used[i] = False

    return ""


print(rearrange("aabbcc", 3))
