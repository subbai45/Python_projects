# Create a Class for a Student:
#
# Define a class Student with attributes for the student's name, age, and marks.
# Create methods to display the student's details.
# Create multiple Student objects and print their details.
def sno(obj):
    while True:
        try:
            sno = int(input(f"Enter the {obj} student number: "))
            if len(str(sno)) == 2:
                return sno
                break
            else:
                print("\tEnter only 2-Digit number")
        except (ValueError,NameError):
            print("\tEnter only Integers with 2-Digits only")
def sname(obj):
    while True:
        try:
            sname = input(f"Enter the {obj} student name(4-10 letters): ").upper()
            if len(sname) <= 10 and len(sname) >= 4 and sname.isalpha():
                return sname
                break
            else:
                print("\tEnter only Alphabets and 4 to 10 letters only")
        except (ValueError,NameError):
            print("\tEnter only Alpha with 4 to 10 letters only")
def age(obj):
    while True:
        try:
            age = int(input(f"Enter the {obj} student's age: "))
            if age >= 15 and age <= 100 and str(age).isdigit():
                return age
                break
            else:
                print("\tAge should be between 15 to 100 years")
        except (ValueError,NameError):
            print("\tAge should be only 2-Digits")
def marks(obj):
    while True:
        try:
            marks = int(input(f"Enter the total marks of {obj} student: "))
            if marks >= 0 and marks <= 100 and str(marks).isdigit:
                return float(marks)
                break
            else:
                print("\tMarks of student should be between 0 to 100")
        except (ValueError,NameError):
            print("\tMarks should be entered only digits")

class student:
    def student_info(self,obj):
        self.sno = sno(obj)
        self.sname = sname(obj)
        self.sage = age(obj)
        self.smarks = marks(obj)

    def display_student_info(self,obj):
        print(f"{obj} student details are {self.__dict__}")


# Main Program
# Creating an objects by using class Student
student1 = student()
student2 = student()
student3 = student()

# Creating an Instance data members
student1.student_info("FRIST")
student1.display_student_info("FIRST")
student2.student_info("SECOND")
student2.display_student_info("SECOND")
student3.student_info("THIRD")
student3.display_student_info('THIRD')
print(" ",student1.__dict__,'\n',student2.__dict__,'\n',student3.__dict__)

