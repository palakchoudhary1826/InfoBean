# 31. Remove duplicate words from a string.
s = input("Enter the String: ")

word = ""
ans = ""
seen = ""


s += " "

for ch in s:

    if ch != " ":
        word += ch
    else:

        found = False
        temp = ""

        
        for c in seen + " ":

            if c != " ":
                temp += c
            else:
                if temp == word:
                    found = True
                    break
                temp = ""

        if not found:
            if ans != "":
                ans += " "
                seen += " "

            ans += word
            seen += word

        word = ""

print(ans)