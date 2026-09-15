row1,col1=map(int,input("Enter Row 1 And Col 1 : ").split())
row2,col2=map(int,input("Enter Row 2 And Col 2 : ").split())
arr1=[]
arr2=[]

if col1==row2:
    print("Fill The 1st Array")

    for i in range(row1):
        row=list(map(int,input(f"Enter {i} row values: ").split()))
        arr1.append(row)

    print("Fill The 2nd Array")

    for i in range(row2):
        row=list(map(int,input(f"Enter {i} row values: ").split()))
        arr2.append(row)

    
    result=[]
    #row1 -> col2 -> col2

    for i in range(row1):
        row=[]
        for j in range(col2):
            total=0
            
            for k in range(col1):
                total+=arr1[i][k]*arr2[k][j]
            
            row.append(total)
        result.append(row)
    
    print(result)

else:
    print("col of 1st array is not equal to row 2nd array ")



    
