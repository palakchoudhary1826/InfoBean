# remove occurrences of a word in a string

s = input("Enter the String: ")
word = input("Enter the Word: ")

# idx = -1;
# subStringSearch=len(s)-len(word)+1
# count=0
s = input("Enter the String: ")
word = input("Enter the Word: ")

new = ""
k = 0

for i in range(len(s)):

    if k > 0:
        k -= 1
        continue

    match = True

    if i + len(word) <= len(s):

        for j in range(len(word)):

            if s[i + j] != word[j]:
                match = False
                break

    else:
        match = False

    if match:
        k = len(word) - 1
    else:
        new += s[i]

print(new)