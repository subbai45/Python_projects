# Employee Class:
#
# Define a class Employee with attributes for employee name, ID, and salary.
# Create methods to display the details and update the salary.
# Create an object of Employee, update the salary, and display the updated details.
import re
import pandas as pd
def name():
    while True:
        try:
            e_name = input("Enter the name of the employee: ").title()
            pattern = r"^[A-Za-z]+(?:\s[A-Za-z]+)*$"
            if re.match(pattern,e_name):
                return e_name
                break
            else:
                print("\tPlease enter valid name")
        except (ValueError,NameError):
            print("\tEnter name correctly--only alphabets")
def ID():
    while True:
        try:
            e_ID = int(input("Enter the ID of the Employee: "))
            pattern = r"^\d{3,4}$"
            if re.match(pattern,str(e_ID)):
                return e_ID
                break
            else:
                print("\tInvalid ID,Enter 3-4 digits only")
        except (ValueError,NameError):
            print("\tPlease enter only digits")

def sal(name):
    while True:
        try:
            e_sal = int(input(f"Enter the {name} salary: "))
            pattern = r"^\d{0,7}$"
            if re.match(pattern,str(e_sal)):
                return float(e_sal)
                break
        except (ValueError,NameError):
            print("\tEnter only digits")

def update(sal):
    while True:
        try:
            update_sal = int(input("Hike incrementation percentage: ")) # 10%
            hike = update_sal / 100 * sal
            return hike
            break
        except (ValueError,NameError):
            print("\tEnter how much % hike need to employee want")
class employee:
    def emp_name(self):
        self.e_name = name()
        self.emp_ID() # calling explicitly
    def emp_ID(self):
        self.e_ID = ID()

    def emp_sal(self):
        self.e_sal = sal(self.e_name)
class salary:
    def emp_sal(self):
        self.e_sal = emp.e_sal

    def emp_update_sal(self):
        self.update_sal = update(self.e_sal)

    def emp_final_sal(self):
        self.final_sal = self.e_sal + self.update_sal

def display(emp,salary):
    print(emp.__dict__)
    print(salary.__dict__)
    '''for key,val in emp.__dict__.items():
        print(key,'--->',val,'type:- ',type(val))'''
    emp_details = pd.Series(emp.__dict__)
    emp_sal = pd.Series(salary.__dict__)
    print("=" * 50)
    print(emp_details)
    print(emp_sal)
# Main Program

emp = employee()
emp.emp_name()
#emp.emp_ID()
emp.emp_sal()
emp_salary = salary()
emp_salary.emp_sal()
emp_salary.emp_update_sal()
emp_salary.emp_final_sal()
print("="*50)
display(emp,emp_salary)
print("="*50)
