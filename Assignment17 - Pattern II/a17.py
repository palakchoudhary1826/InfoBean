'''
Docstring for Assignment17(Pattern-II).a17
Enter The Number  : 5

* 
# # 
* * * 
# # # # 
* * * * * 
'''

n=int(input("Enter The Number  : "))

i=0
while i<=n:
    j=0
    while j<i:
        if i%2!=0:
            print("*",end=" ")
        else:
            print("#",end=" ")
        j+=1
    print()
    i+=1
