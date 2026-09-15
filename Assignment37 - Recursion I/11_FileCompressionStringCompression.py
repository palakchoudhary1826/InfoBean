'''
Assignment 11: File Compression System (String Compression)

A file compression company wants to reduce the size of text files before storing them. One simple compression technique is to replace consecutive repeated characters with the character followed by its count.

For example:

AAABBCCCCD → A3B2C4D1

Task:
Write a recursive function that compresses a string by counting consecutive occurrences of each character.

Input:
Enter a String:
AAABBCCCCD

Output:
Compressed String = A3B2C4D1

Sample Input 2:
Enter a String:
WWWWXXYYZ

Sample Output 2:
Compressed String = W4X2Y2Z1

Sample Input 3:
Enter a String:
AAAAA

Sample Output 3:
Compressed String = A5
'''
new=""
ch=""
count=0
def compress(a,i):
    global new,ch,count
    if i==len(a):
        new+=ch+str(count)
        return
    

    
    if ch!=a[i]:
        if ch!='':
            new+=ch+str(count)
        ch=a[i]
        count=1
    
    else:
        count+=1
    
    compress(a,i+1)
    

compress("wwwxxyyz",0)
print(new)




    
    