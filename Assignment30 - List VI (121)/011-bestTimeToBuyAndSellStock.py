'''
Problem 11: Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a
given stock on the ith day.

You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that
stock.

Return the maximum profit you can achieve.

If you cannot achieve any profit, return 0.

Example 1:
Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5

Explanation:
Buy on day 2 at price 1 and sell on day 5 at price 6.
Profit = 6 - 1 = 5.

Example 2:
Input:
prices = [7, 6, 4, 3, 1]

Output:
0

Explanation:
There is no way to make a positive profit.

Constraints:
- You must buy before you sell.
- You can complete at most one transaction.
'''

l=[7, 1, 5, 3, 6, 4]

minPrice=len(l)
maxprofit=0

for i in l: #i -> day
    if i<minPrice:
        minPrice=i # meine stock ko kharida 

    profit=i-minPrice
    if profit>maxprofit:
        maxprofit=profit
  
 

print(minPrice)
print(maxprofit)
