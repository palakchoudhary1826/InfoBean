# Check if two strings are anagrams

s1=input('Enter The String I: ')

s2=input('Enter The String II: ')


ans=True
if len(s1)!=len(s2):
    ans=False

else:

    
    for i in s1:

        c1=0
        for j in s2:
            if i==j:
                c1+=1

        c2=0

        for k in s1:
            if i==k:
                c2+=1

        if c1!=c2:
            ans=False
            break


if ans:
    print("ana")
else:
    print("not ana")    

                
        
