class employe:
    def __init__(self, emp_id, emp_name,department,salary):
        self.pro_id = emp_id
        self.pro_name = emp_name
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.salary = salary

    def display_info(self):
        return f"Employee ID: {self.emp_id}, Employee Name: {self.emp_name}, Department: {self.department}, Salary: {self.salary}"