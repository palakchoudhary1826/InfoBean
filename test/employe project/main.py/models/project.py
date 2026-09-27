class projects:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"
    