# to find the avg marks of student by dynamically

n=int(input("Enter the how many records to be entered: "))
student_marks={}
for _ in range(n):
    name,*marks=input().split()
    scores=[float(val) for val in marks]
    student_marks[name]=scores
print()
print(student_marks)