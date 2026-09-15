def permutation(s):

    current = []

    return backtrack(s, current)


def backtrack(s, current):

    # base case

    if len(current) == len(s):
        print("".join(current))

        return 1

    # revursive case:
    count = 0

    for i in range(len(s)):

        # choose

        current.append(s[i])

        # explore

        count += backtrack(s, current)

        # undo

        current.pop()
    return count


count=permutation("ABC")
print(count)
