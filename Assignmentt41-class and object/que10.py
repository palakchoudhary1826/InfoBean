"""Assgnment 10: Personal Expense Calculator
 A person wants to calculate monthly expenses and savings.
Create a class ExpenseTracker with the following attributes:
Person name
Monthly salary
Rent
Food expenses
Travel expenses
Other expenses
Create the following methods:
calculate_total_expenses() – Calculate all expenses.
calculate_savings() – Calculate salary minus total expenses.
display_expense_report() – Display salary, expenses, and savings.
Formula:
Total Expenses = Rent + Food + Travel + Other Expenses
Savings = Monthly Salary - Total Expenses
Sample data:
Monthly Salary: 60000
Rent: 12000
Food: 8000
Travel: 5000
Other Expenses: 3000
Expected result:
Total Expenses: 28000
Savings: 32000"""

class expensetracker():
    def accept(self,person_name,month_salary,rent,food_exp,travel_exp,other_exp):
        self.person_name=person_name
        self.month_salary=month_salary
        self.rent=rent
        self.food_exp=food_exp
        self.travel_exp=travel_exp
        self.other_exp=other_exp
    def total_expenses(self):
        self.toatal_exp=self.rent+self.food_exp+self.travel_exp+self.other_exp
    def savings(self):
        self.save=self.month_salary-self.toatal_exp
    def display(self):
        print("Person name=",self.person_name)
        print("Monthly salary=",self.month_salary)
        print("Rent=",self.rent)
        print("Food=",self.food_exp)
        print("Travel=",self.travel_exp)
        print("Other expenses=",self.other_exp)
        print("Total expenses=",self.toatal_exp)
        print("savings=",self.save)
e=expensetracker()
e.accept("ajay",60000,12000,8000,5000,3000)
e.total_expenses()
e.savings()
e.display()


