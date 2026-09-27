"""Rithish is developing a straightforward pizza ordering system. To achieve this, he needs a Pizza class with a constructor for
 the base price and topping cost, along with a calculatePrice method overriding. He also wants a DiscountedPizza class that inherits from
Pizza, applying a 10% discount for more than three toppings.

The program prompts the user for inputs, creates instances of both classes, calculates regular and discounted prices,
and displays them formatted appropriately.

Example 1

Input:
9.5
1.25
3
Output:
Price without discount: Rs.13.25
Price with discount: Rs.13.25
Explanation:
Rithish orders a pizza with a base price of Rs. 9.5, a topping cost of Rs. 1.25, and selects 3 toppings. The price is calculated as 9.5 + (1.25 * 3) = 13.25. The regular and discounted prices are both Rs. 13.25, as no discount has been applied.

Example 2

Input:
11.0
2.0
7
Output:
Price without discount: Rs.25.00
Price with discount: Rs.22.50
Explanation:
Rithish orders another pizza with a higher base price of Rs. 11.0, a topping cost of Rs. 2.0, and chooses 7 toppings.
Regular Price: 11.0 + (2.0 * 7) = Rs. 25.00.
Discounted Price: The discounted price is calculated as 90% of the regular price, i.e., 0.9 * 25.00 = Rs.22.50.
Input format :
The first line of input consists of a double value, representing the base price of the pizza.
The second line consists of a double value, representing the cost per topping.
The third line consists of an integer, representing the number of toppings chosen for the pizza.
Output format :
The first line of output prints the price without discount, rounded off to two decimal places.
The second line prints the price with the discount, rounded off to two decimal places.

Refer to the sample output for formatting specifications.
Code constraints :
The base price and the cost per topping should be greater than zero.
1 ≤ number of toppings ≤ 10
Sample test cases :
Input 1 :
9.5
1.25
3
Output 1 :
Price without discount: Rs.13.25
Price with discount: Rs.13.25
Input 2 :
11.0
2.0
7
Output 2 :
Price without discount: Rs.25.00
Price with discount: Rs.2"""
"""
class Pizza:

    def __init__(self, base_price, topping_cost):
        self.base_price = base_price
        self.topping_cost = topping_cost

    def calculatePrice(self, toppings):
        return self.base_price + (self.topping_cost * toppings)


class DiscountedPizza(Pizza):

    def calculatePrice(self, toppings):
        price = self.base_price + (self.topping_cost * toppings)

        if toppings > 3:
            price = price - (price * 10 / 100)

        return price


base_price = float(input("enter the base price"))
topping_cost = float(input("enter the topping cost"))
toppings = int(input("enter the toppings"))

p = Pizza(base_price, topping_cost)
dp = DiscountedPizza(base_price, topping_cost)

price1 = p.calculatePrice(toppings)
price2 = dp.calculatePrice(toppings)

print(f"Price without discount: Rs.{price1:.2f}")
print(f"Price with discount: Rs.{price2:.2f}")
"""

"""Matrix Multiplication

Write a Python program to read two matrices from the user and perform matrix multiplication.

Before multiplying the matrices, check whether multiplication is possible. Matrix multiplication is possible only if
the number of columns in the first matrix is equal to the number of rows in the second matrix.

Requirements
Read the number of rows and columns for the first matrix.
Read all the elements of the first matrix from the user.
Read the number of rows and columns for the second matrix.
Read all the elements of the second matrix from the user.
Check whether matrix multiplication is possible.
If possible, multiply the matrices using nested loops.
Display the resulting matrix.

If multiplication is not possible, display:

Matrix multiplication is not possible"""

"""
row=int(input("Enter row size of first matrix:"))
col=int(input("Enter column size of first matrix:"))

row1=int(input("Enter row size of second matrix :"))
col1=int(input("Enter column size of second matrix:"))

if col==row1:

	print("Elements of first matrix")
	matrix=[]
	for i in range(row):
		r=[]
		for j in range(col):
			r.append(int(input("Enter element {} of Matrix 1 :".format(i))))
		matrix.append(r)
	print()
	for r in matrix:
		print(*r)
	print("Elements of Second matrix")
	matrix1=[]
	for i in range(row1):
		r=[]
		for j in range(col1):
			r.append(int(input("Enter element {} of matrix 2 :".format(i))))
		matrix1.append(r)
	print()
	for r in matrix1:
		print(*r)
	print()
	result=[]
	for i in range(row):
		r=[]
		for j in range(col1):
			r.append(0)
		result.append(r)
	for i in range(row):
		for j in range(col1):
			for k in range(col):
				result[i][j]=result[i][j]+matrix[i][k]*matrix1[k][j]
	print(result)
	for r in result:
		print(*r)
		
else:
	print("multipliction not possible")
    """