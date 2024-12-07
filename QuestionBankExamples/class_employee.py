# 2)  Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and
# methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "RAJESH", "E7876", 50000, "ACCOUNTING"
# "RAKESH", "E7499", 45000, "RESEARCH"
# "RAM", "E7900", 50000, "SALES"
# "RAJIT", "E7698", 55000, "OPERATIONS"
# =>Use 'assign_department' method to change the department of an employee.
# =>Use 'print_employee_details' method to print the details of an employee.
# =>Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked,
# which is the number of hours worked by the employee. If the number of hours worked is more than 50, the
# method computes overtime and adds it to the salary. Overtime is calculated as following
# formula:
# =>overtime = hours_worked - 50
# =>Overtime amount = (overtime * (salary / 50))

import re
def e_name(name):
    while True:
        try:
            emp_name = input(f"Enter the name of {name} employee: ").title()
            res = 1
            for val in emp_name:
                if not val.isalpha() and val.isspace():
                    res += 1
            if res == 1:
                return emp_name
                break
            else:
                print(f"{emp_name} is Invalid Name")
        except (ValueError or TypeError):
            print("Please Enter valid input--Try Again!")

def e_id(id):
    while True:
        try:
            emp_id = int(input(f"Enter the I'd of the {id} employee: "))
            if str(emp_id).isdigit():
                return emp_id
                break
            else:
                print(f"{emp_id} is Not valid I'd")
        except (ValueError or TypeError):
            print("Please enter valid input--Try Again!")
def e_sal(sal):
    while True:
        try:
            emp_sal = float(input(f"Enter the salary of {sal} employee: "))
            # r'^[-+]?[0-9]*\.?[0-9]+$'
            validation = re.search(r'^[-+]?[0-9]*\.?[0-9]+$',str(emp_sal))
            if validation != None:
                return emp_sal
                break
            else:
                print(f"Invalid salary")
        except (ValueError or TypeError):
            print("Please enter valid input--Try Again!")

def job_title(job):
    while True:
        try:
            emp_job_title = input(f"Enter the Job Department of the {job} employee: ")
            if emp_job_title.isalpha():
                break
            else:
                print(f"{emp_job_title} is not Valid Department")
        except (ValueError or TypeError):
            print("Please enter valid input--Try again!")


class Employee:
    def __init__(self,emp):
        self.emp_id = e_id(emp)
        self.emp_name = e_name(emp)
        self.emp_salary = e_sal(emp)
        self.emp_job = job_title(emp)

    def calculate_emp_salary(self,sal):
        emp_sal = self.emp_salary
# =>overtime = hours_worked - 50
# =>Overtime amount = (overtime * (salary / 50))

    def emp_assign_department(self):pass
    def print_employee_details(self):
        for val,var in self.__dict__.items():
            print(f"{val}--->{var}")

# Main Program
emp1 = Employee('First')
emp2 = Employee('Second')
'''emp3 = Employee('Third')
emp4 = Employee('Fourth')'''

emp1.calculate_emp_salary()
emp1.print_employee_details()
emp2.print_employee_details()
'''emp3.print_employee_details()
emp4.print_employee_details()'''


