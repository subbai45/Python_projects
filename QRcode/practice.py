"""'''def studentmarks(i):
    marks=float(input("Enter the {} marks: ".format(i)))
    return marks

lst=[['c','c++','python'],['c','c++','python']]
print(lst)
dmarks={}
for val in lst:
    for i in val:
        dmarks[i]=studentmarks(i)
print(dmarks)'''
'''def studentmarks(subject):
    marks = float(input(f"Enter the marks for {subject}: "))
    return marks

# List of lists of subjects
lists_of_subjects = [['C', 'C++', 'Python'], ['C', 'C++', 'Python']]

# Dictionary to store marks for each list of subjects
dmarks = {}

# Loop through each list and store marks separately
for idx, subject_list in enumerate(lists_of_subjects, start=1):
    student_key = f"List_{idx}"  # Create a key for each list (e.g., List_1, List_2)
    dmarks[student_key] = {}     # Initialize a nested dictionary for each list
    for subject in subject_list:
        dmarks[student_key][subject] = studentmarks(subject)

# Print the dictionary with subjects and marks for each list
print(dmarks)'''
'''from prettytable import PrettyTable
st_id = [45,55,24]
st_name = ['rohit','shirley','subbai']
sub = [['c','c++','py'],['c','c++','py'],['c','c++','py']]
marks = [[24,45,55],[24,45,55],[24,45,55]]
grade = ['A','B','A+']
per = ['55%','55%','55%']'''
'''
columns = ['STUDENT_ID','STUDENT_NAME']
my_table = PrettyTable(columns)
# write code here
for i in range(len(st_id)):
    my_table.add_row([st_id[i],st_name[i]])
print(my_table)'''

'''columns = ['STUDENT_ID', 'STUDENT_NAME', 'SUBJECTS', 'MARKS', 'GRADE', 'PERCENTAGE']
my_table = PrettyTable()
my_table.add_column(columns[0], st_id)
my_table.add_column(columns[1],st_name)
my_table.add_column(columns[2],sub)
my_table.add_column(columns[3],marks)
my_table.add_column(columns[4],grade)
my_table.add_column(columns[5],per)
print(my_table)'''

def total_marks(name,marks):
    t_marks = {}
    t_marks[name] = marks
    print(t_marks)


def student_grade(marks):
   if marks[key] >= 90:
            return 'A+'
        elif marks[key] >= 75 and marks[key] < 90:
            return 'A'
        elif marks[key] >= 60 and marks[key] < 75:
            return 'B+'
        elif marks[key] >= 45 and marks[key] < 60:
            return 'B'
        elif marks[key] >= 35 and marks[key] < 45:
            return 'C'
        else:
            return 'F'



dmarks = {'ROHIT': {'C': 45.0, 'C++': 55.0, 'PYTHON': 65.0},
 'SUBBAI': {'C': 18.0, 'C++': 28.0, 'JAVA': 38.0},
 'SHIRLEY': {'C': 2.0, 'DS': 3.0, 'C#,NET': 4.0},
 'HEERA': {'COM': 11.0, 'STATS': 11.0, 'MARKETING': 11.0},
 'fgurh': {'COM': 28.0, 'PHYSICS': 28.0, 'MATHS': 28.0}}
print(len(dmarks))
t_marks = {}
for val in dmarks.items():
    print(val)
    sum_marks=sum(val[1].values())
    print(sum_marks)
    #total_marks(val[0],sum_marks)
    t_marks[val[0]] = sum_marks
print(t_marks)
grade = []
total_subjects = 3
total_m = total_subjects * 100

for val in t_marks:
    print(round((t_marks[val]/total_m)*100,2))
   # grade.append(student_grade(t_marks))

"""
'''dmarks = {'ROHIT': {'C': 45.0, 'C++': 55.0, 'PYTHON': 65.0},
 'SUBBAI': {'C': 18.0, 'C++': 28.0, 'JAVA': 38.0}}

for val in dmarks.values():
    print(len(val.values()))'''

lst = [2,3]
dic = {'SUBBAI': 298.0, 'SHIRLEY': 261.0}
for dicn,val in zip(dic,lst):
    print(dicn,val)
    print("-"*40)