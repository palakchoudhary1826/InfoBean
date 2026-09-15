'''
Docstring for Assignment23 - String VI.a03
Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

• Keep the first occurrence unchanged.
• Add (1), (2), (3)... for duplicate filenames.

Write a Python program to rename duplicate filenames.

Input:
file file image file image data

Output:
file file(1) image file(2) image(1) data
'''

n=input("Enter : ")
new=""
done="file image"
# first=False

for word in n.split():
    temp=0

    for w in done.split():
        if word==w:
            temp+=1
    
    if temp==0:
        new+=word+" "
       
    else:
        
        new+=word+"("+str(temp)+") " # file(1)
    done+=word+" "

print(new)
