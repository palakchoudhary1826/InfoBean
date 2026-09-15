'''
Docstring for Assignment23 - String VI.a01
. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

```text
abcabcbb
```

Output:

```text
abc
```
'''

s=input("Enter:")

ans=""

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        # print(sub)
        count=0

        for k in range(len(s)-len(sub)+1):
            match=True

            for m in range(len(sub)):
                if s[k+m]!=sub[m]:
                    print(s[k+m],sub[m])
                    match=False
                    break
            
            if match:
                count+=1
        
        if count>=2 and len(sub)>len(ans):
            ans=sub

print(ans)



    
