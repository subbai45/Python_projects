from prettytable import PrettyTable

# Function to take and validate student ID input
def student_id():
    while True:
        id = input("Enter the Student's ID: ")
        if id.isdigit():
            return id
        else:
            print("Invalid ID, please enter a valid numeric ID.")

# Function to take and validate student name input
def student_name():
    while True:
        name = input("Enter the Student's Name: ").upper()
        if name.isalpha():
            return name
        else:
            print("Invalid name, please enter a valid alphabetic name.")

# Function to input subjects for each student
def subjects():
    while True:
        sub = input("Enter the total number of subjects: ")
        if sub.isdigit():
            subs = []
            for i in range(1, int(sub) + 1):
                var = input(f"Enter the name of subject {i}: ").upper()
                subs.append(var)
            return subs
        else:
            print("Invalid input, please enter a valid number for subjects.")

# Function to input marks for a given subject and student
def student_marks(sub, name):
    while True:
        try:
            marks = float(input(f"Enter the marks for {sub} (0-100) for {name}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input, please enter a valid number.")

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'

# Function to calculate and display student details in a table
def student_details(students, dmarks):
    columns = ['STUDENT_ID', 'STUDENT_NAME', 'TOTAL SUBJECTS', 'TOTAL MARKS', 'AVERAGE', 'PERCENTAGE', 'GRADE']
    my_table = PrettyTable()
    my_table.field_names = columns

    # Loop through each student and calculate total, average, percentage, and grade
    for student in students:
        total_marks = sum(dmarks[student['name']].values())
        total_subjects = len(dmarks[student['name']])
        average = total_marks / total_subjects
        percentage = (total_marks / (100 * total_subjects)) * 100
        grade = calculate_grade(percentage)

        my_table.add_row([student['id'], student['name'], total_subjects, total_marks, f"{average:.2f}", f"{percentage:.2f}%", grade])

    print(my_table)
    return my_table

# Main program
total_students = int(input("Enter the total number of students in the class: "))
students = []
dmarks = {}

for i in range(total_students):
    student = {}
    student['id'] = student_id()
    student['name'] = student_name()
    student['subjects'] = subjects()
    students.append(student)

    dmarks[student['name']] = {}
    for subject in student['subjects']:
        dmarks[student['name']][subject] = student_marks(subject, student['name'])
        print(dmarks)
# Display results
my_table = student_details(students, dmarks)
try:
    with open (f"{input("Enter the file name to store the data: ")}", "a+") as fp:
        fp.write(str(my_table))
        fp.seek(0)
        my_table_data = fp.read()
        print(my_table_data)
except (FileNotFoundError,FileExistsError):
    print("Please enter valid file name or existing file name")
