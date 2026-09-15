'''
3. Online Shopping Discount (Using filter() and map() with Lambda Expressions)

An online shopping website is running a Festive Sale. Customers who purchase products worth ₹2,000 or more are eligible for a 20% discount.

Task:
Write a Python program to:
1. Filter the prices of products that are ₹2,000 or more.
2. Calculate the discounted price by applying a 20% discount.
3. Display the final discounted prices.

Note:
Use filter() to identify eligible products and map() to calculate the discounted prices. Both operations must use lambda expressions.

Input Format:
The first line contains an integer N, representing the number of products.
The second line contains N space-separated product prices.

Output Format:
Display the discounted prices of all eligible products.

Sample Input:
Enter the number of products:
6

Enter the product prices:
1500 2500 1800 3000 4500 1200

Sample Output:
Discounted Prices:
2000.0 2400.0 3600.0
'''

def discount (i):
    return i-(i/5)


l=list(map(int,input("Enter Product Prices : ").split()))

PriceFilter=list(filter(lambda x : x>=2000,l))
print(PriceFilter)
result=map(discount,PriceFilter)

print(list(result))