"""
Compare the Number of Times 'the' and 'is' Appear

Write a Python program to input a string and count how many
times the words "the" and "is" appear.

The comparison should be case-insensitive.

Display which word appears more times.

Input:
Enter a string: The sky is beautiful. The weather is good.

Output:
'the' : 2
'is'  : 2
Both appear equal number of times.
"""

s=input("Enter The String : ").lower()

sub1="the"
sub2="is"

count1=0
count2=0

for i in range(len(s)-len(sub1)+1):

    if s[i:i+len(sub1)]==sub1:  # noqa: SIM102
        if (i==0 or s[i-1]==" ") and (i+len(sub1)==len(s) or s[i+len(sub1)]==" "):
            count1+=1

for i in range(len(s)-len(sub2)+1):

    if s[i:i+len(sub2)]==sub2:  # noqa: SIM102
        if (i==0 or s[i-1]==" ") and (i+len(sub2)==len(s) or s[i+len(sub2)]==" "):
            count2+=1

print(f"'the' : {count1}")
print(f"'is'  : {count2}")

if count1>count2:
    print("'the' appears more than 'is'")
elif count1<count2:
    print("'is' appears more than 'the'")
else:
    print("Both appear equal number of times")
