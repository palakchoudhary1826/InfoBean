# 25. Count total number of words in a string

s=input("Enter The String : ")
count=0

for i in s.split():
    count+=1

print(count)