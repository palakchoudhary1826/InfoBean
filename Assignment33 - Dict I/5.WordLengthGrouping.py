"""
=========================================
5. WORD LENGTH GROUPING
=========================================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store the result in a dictionary.

Sample Output:
{
    3: ['api', 'css'],
    4: ['java', 'html'],
    5: ['react'],
    6: ['python']
}
"""

tags=list(map(str,input("Enter The Tags : ").split()))
print(tags)
print()

d={}
for i in tags:
    d[len(i)]=d.get(len(i),[])+[i]

# print(d)

d=dict(sorted(d.items()))
d=sorted(d.items()) # gave in list[tuple()]

print(d)

