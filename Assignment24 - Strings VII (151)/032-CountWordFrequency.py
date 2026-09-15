s = input("Enter the String: ")

words = []
word = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words = words + [word]
            word = ""

if word != "":
    words = words + [word]

visited = []

for i in range(len(words)):

    found = False

    for j in range(len(visited)):
        if words[i] == visited[j]:
            found = True
            break

    if not found:

        count = 0

        for j in range(len(words)):
            if words[i] == words[j]:
                count += 1

        print(words[i], ":", count)
        visited = visited + [words[i]]