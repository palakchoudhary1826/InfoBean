# Secure Password Analysis

# A cybersecurity team wants to identify pairs of passwords having no common characters.

# Problem Statement:

# Given N strings, count the number of pairs that do not share any common character.

# Example:

# Input

# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}

# Output

# 4

# Explanation

# ('abc', 'de')
# ('abc', 'fg')
# ('de', 'fg')
# ('fg', 'ad')


arr = list(map(str, input("Enter The Strings : ").split(" ")))
print(arr)
print()

count = 0
seen = []

for i in range(len(arr)):
    former = arr[i]

    for j in range(i + 1, len(arr)):
        latter = arr[j]

        match=False

        for ch in former:
            if ch in latter:
                match=True
                break
        if not match:
            count+=1
            print(f"{former,latter}")

      

print(count)



