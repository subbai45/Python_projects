'''# to find the sstudents average marks

if __name__ == '__main__':
    n = int(input())
    if 2 <= n <= 10:
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            if len(scores) != 3:
                break
            if any(not(0 <= mark <= 100) for mark in scores ):
                break
            student_marks[name] = scores
        query_name = input()
        print(student_marks)

        for val in student_marks:
            #print(val,type(val))
            if val == query_name:
                marks = student_marks[val]
                print(marks)
                avg= sum(marks)/len(marks)
        print(round(avg,2))


'''
if __name__ == '__main__':
    n = int(input("Enter the number of students: "))

    # Check the constraint for the number of students
    if not (2 <= n <= 10):
        print("Number of students must be between 2 and 10.")
        exit()

    student_marks = {}

    # Taking input for student marks
    for _ in range(n):
        name, *line = input(f"Enter the name and 3 marks for student {_ + 1}: ").split()
        scores = list(map(float, line))

        # Check the constraint for the number of marks
        if len(scores) != 3:
            print(f"Each student must have exactly 3 marks.")
            exit()

        # Check the constraint for marks range
        if any(not (0 <= mark <= 100) for mark in scores):
            print("Marks must be between 0 and 100.")
            exit()

        student_marks[name] = scores

    query_name = input("Enter the name of the student to query: ")

    avg = None  # Initialize avg to None to handle cases where name is not found

    # Print student_marks dictionary (for debugging)
    print(student_marks)

    # Loop through the student_marks dictionary
    for val in student_marks:
        if val == query_name:
            marks = student_marks[val]
            avg = sum(marks) / len(marks)  # Calculate the average

    if avg is not None:
        print(round(avg, 2))  # Print average if found
    else:
        print(f"No student found with the name {query_name}")
