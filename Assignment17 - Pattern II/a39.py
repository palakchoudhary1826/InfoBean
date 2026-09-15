'''
Docstring for Assignment17(Pattern-II).a39
123456
54321
1234
321
12
1

'''

n=int(input("Enter The NUmber : "))

i=1
while i<=n:
    
    if i%2!=0:
        j=1
        while j<=n-i+1:
            print(j,end=" ")
            j+=1
    else :
        j=n-i+1
        while j>=1:
            print(j,end=" ")
            j-=1
    
    print()
    i+=1
        

