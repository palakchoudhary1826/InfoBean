"""
=========================================
3. WEBSITE PAGE VISIT TRACKER
=========================================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time
"""

pages=list(map(str,input("Enter The page visit : ").split()))
print(pages)
d={}
for i in pages:
    d[i]=d.get(i,0)+1


print("Dictionary ", d)

for i in d.items():
    print(f"{i[0]} visited {i[1]} times")