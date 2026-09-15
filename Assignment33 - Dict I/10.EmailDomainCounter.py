"""
=========================================
10. EMAIL DOMAIN COUNTER
=========================================

emails = [
    "ajay@gmail.com",
    "ravi@yahoo.com",
    "neha@gmail.com",
    "aman@outlook.com",
    "abc@gmail.com"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
    'gmail.com': 3,
    'yahoo.com': 1,
    'outlook.com': 1
}
"""

emails = [
    "ajay@gmail.com",
    "ravi@yahoo.com",
    "neha@gmail.com",
    "aman@outlook.com",
    "abc@gmail.com"
]

# domain=[]
d={}

for i in emails:
    for j in range(len(i)):
        if i[j]=='@' and i[j-1]!='@':
            domain=i[j+1:]
            d[domain]=d.get(domain,0)+1


# print(domain)

# for i in domain:
#     d[i]=d.get(i,0)+1

print(d)