class Employe:
    def __init__(self,emp_id,name,salary,department):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
       print(f"{self.emp_id} {self.name} {self.salary} {self.department}")  

        