import sys
import pandas as pd
class student:
    def student_info(self,obj):

        self.sno = int(input(f"Enter the {obj} students number: "))
        self.sname = input(f"Enter the {obj} students name: ").upper()
        self.smarks = float(input(f"Enter the {obj} students marks: "))
    def display_student_info(self,obj):
        print("=" * 50)
        print(f"{obj} student info")
        print("=" * 50)
        print(f"Address of {obj} student is {id(self)}")
        print(f"{obj} student details {self.__dict__}")
        print(f"{obj} size {sys.getsizeof(self.__dict__)}")
        return self.__dict__

class teacher:
    def teacher_info(self,obj):
        self.sno = int(input(f"Enter the {obj} teacher number: "))
        self.name = input(f"Enter the {obj} teacher name: ").upper()
        self.sub = input(f"Enter the {obj} teacher subject: ").upper()
    def display_teacher_info(self,obj):
        print(f"{obj} teacher details\n")
        print(f"{obj} teacher details {self.__dict__}")
        return self.__dict__
def csv_file(data):pass



# Main program
s1 = student()
s2 = student()
t1 = teacher()
t2 = teacher()

print("="*50)
s1.student_info("first")
print("Address of student-1",id(s1))
print("-"*50)
s2.student_info("second")
print("Address of student-2",id(s2))

# displaying the students data
s1_data = s1.display_student_info("first")
s2_data = s2.display_student_info("second")
print(s1_data)
print(s2_data)

#initiallizing the teachers data
t1_data = t1.teacher_info("First")
t2_data = t2.teacher_info("Second")

# displaying the teachers data
t1.display_teacher_info("First")
t2.display_teacher_info("Second")

csv_file(s1_data)