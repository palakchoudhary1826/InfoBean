'''
Docstring for Assignment23 - String VI.a02
Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

No unique digit found

Input:
A122334455667789

Output:
1
'''

n=input("enter : ")
found=False

for i in n:

    if i in "0123456789":
        count=0
        for j in n:
            if i==j:
                count+=1
        
        if count==1:
            print(i)
            found=True
            break

if not found:
    print("no unique digit found")


