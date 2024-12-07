# to take the inputs of marks,student number,various subjects, and display the total marks,average and percentage
# and also print the grade of the student
import csv
import pickle
from prettytable import PrettyTable
def student_id():
    while True:
        id = input("Enter the Student's I'd: ")
        if (id.isdigit()):
            return id
            break
        else:
            print("Invalid I'd, Please Enter the valid I'd")
def student_name():
    while True:
        name = input("Enter the Student's Name: ").upper()
        if (name.isalpha()):
            return name
            break
        else:
            print("Invalid I'd, Please Enter the valid I'd")

def subjects(name):
    while True:
        sub=input("Enter the total subjects: ")
        if(sub.isdigit()):
            i=1
            subs=[]
            while(i<=int(sub)):
                var=input("Enter the {}th subject: ".format(i)).upper()
                subs.append(var)
                i += 1
            return subs
            break
        else:
            print("Invalid subject,Please enter only digits")
def student_marks(sub,nam):
    while True:
        try:
            marks = float(input(f"Enter the {sub}(0 - 100) marks of {nam}: "))
            if 0 <= marks <=100:
                return marks
            else:
                print("invalid marks, Please enter from 0 to 100 ")
        except ValueError:
            print("Enter only digits, Please enter only number")

def total_marks(dmarks):
    t_marks = {}
    for val in dmarks.items():
        sum_marks = sum(val[1].values())
        t_marks[val[0]] = sum_marks
    return t_marks

def student_grade(marks,sub):
    sum_of_marks = sub * 100
    per = (marks/sum_of_marks)*100
    if per >= 90:
        return 'A+'
    elif 80 <= per < 90:
        return 'A'
    elif 70 <= per < 80:
        return 'B+'
    elif 60 <= per < 70:
        return 'B'
    elif 50 <= per < 60:
        return 'C'
    elif 35 <= per < 50:
        return 'D'
    else:
        return 'F'

def store_in_pretty_table(st_id, st_name, st_subjects, t_marks, len_sub, grade):
    # Create PrettyTable instance
    my_table = PrettyTable()

    # Define the columns for the table
    my_table.field_names = ['STUDENT_ID', 'STUDENT_NAME','STUDENT SUBJECTS','TOTAL SUBJECTS', 'TOTAL MARKS', 'AVERAGE', 'PERCENTAGE',
                            'GRADE']

    # Add rows for each student
    for i in range(len(st_id)):
        total_subjects = len_sub[i]
        total_marks = t_marks[st_name[i]]
        student_subjects = st_subjects[i]
        average = total_marks / total_subjects
        percentage = (total_marks / (total_subjects * 100)) * 100
        student_grade = grade[st_name[i]]

        # Add the row to the table
        my_table.add_row(
            [st_id[i], st_name[i],student_subjects, total_subjects, total_marks, f"{average:.2f}", f"{percentage:.2f}%", student_grade])

    # Print the table
    print(my_table)
    return my_table

#Main program
total_students=int(input("Enter the total students in the class: "))
st_id=[]
st_name=[]
st_subjects=[]
i=1

while(i<=total_students):
    st_id.append(student_id())
    st_name.append(student_name())
    st_subjects.append(subjects("st_name"))
    i += 1
dmarks = {}

# Loop through each student and store their marks
for val, name in enumerate(st_name):
    subjects = st_subjects[val]

    # Create a nested dictionary for each student's subjects
    dmarks[name] = {}

    # Collect marks for each subject
    for subject in subjects:
        dmarks[name][subject] = student_marks(subject,name)

len_sub = []
print(dmarks)
# length of the each student subject's stored in list
for val in dmarks.values():
    len_sub.append(len(val.values()))

#finding the sum of the marks of each student and storing in the list pf t_marks
t_marks = total_marks(dmarks)

# finding the grade of the each student by their percentage
grade = {}
for t_m,val in zip(t_marks,len_sub):
    # print(f"grade for {t_m} is {student_grade(t_marks[t_m],val)}")
    grade[t_m] = student_grade(t_marks[t_m],val)

print("students id: ",st_id)
print("students name: ",st_name)
print("students subjects: ",st_subjects)
print("total marks: ",t_marks)
print("len of subjects: ",len_sub)
print("grade of students: ",grade)
print("\n\n")
