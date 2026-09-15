# Get the Unicode code point before a given index.

s = input("Enter The String : ")
idx = int(input("Enter The Index : "))

if 1 <= idx < len(s):
    ch = s[idx - 1]
    print("Character Before Index :", ch)
    print("Unicode Code Point :", ord(ch))
else:
    print("No character exists before the given index.")