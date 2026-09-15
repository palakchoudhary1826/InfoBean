'''
Docstring for a68
        # 
      * # *
    * * # * *
  * * * # * * *
* * * * # * * * *
'''

n=int(input("Enter The  Number "))

i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1

    
    k=1
    
    while k<=i-1:        
        print("*",end=" ")
        
        k+=1
    
    print("#",end=" ")
        
    l=1
    
    while l<=i-1:        
        print("*",end=" ")
        l+=1
        
    print()
   
    i+=1


    
