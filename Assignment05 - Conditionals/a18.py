'''

A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500
'''
a,b,c,d,e,f=map(int,input("Enter the Stock of 6 unit sperated by Comma(,) : ").split(","))

high=0;

if a>b:
    if a>c:
        if a>d:
            if a>e:
                if a>f:
                    high=a
                else:
                    high=f 
            else:
                if e>f:
                    high=e 
                else:
                    high=f 
        else:
            if d>e:
                high=d
            else:
                if e>f:
                    high=e 
                else:
                    high=f 
    else:
        if c>d:
            if c>e:
                if c>f:
                    high=c 
                else:
                    high=f 
            else:
                if e>f:
                    high=e 
                else:
                    high=f 
        else:
            if d>e:
                high=d
            else:
                if e>f:
                    high=e 
                else:
                    high=f 
        

else:
    if b>c:
        if b>d:
            if b>e:
                if b>f:
                    high=b 
                else:
                    high=f 
            else:
                if e>f:
                    high=e 
                else:
                    high=f
        else:
            if d>e:
                high=d
            else:
                if e>f:
                    high=e 
                else:
                    high=f 
    else:
        if c>d:
            if c>e:
                if c>f:
                    high=c
                else:
                    high=f 
            else:
                if e>f:
                    high=e 
                else:
                    high=f
        else:
            if d>e:
                if d>f:
                    high=d
                else:
                    high=f 
            else:
                if e>f:
                    high=e 
                else:
                    high=f 
               
                       
                    
    
print(f"Highest Stock : {high}")