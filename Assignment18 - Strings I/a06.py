"""
Docstring for Assignment18.a06

Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
"""

n=input("enter the PNR : ")
c=0
if len(n)==12: 
    if n.startswith("PNR"):
        i=3
        while i<len(n):
            if not (n[i]>='0' and n[i]<='9'):
                c=1
                break
            
            i+=1
    if c==1:
        print("invalid")
    else:
        print("valid")
else:
    print("Invalid length")






