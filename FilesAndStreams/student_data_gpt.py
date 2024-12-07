import pickle
from prettytable import PrettyTable

# Function to insert student data dynamically
def insert_data():
    try:
        # Collect input data
        st_id = int(input("Enter the student ID: "))
        st_name = input("Enter the student name: ").upper()
        st_marks = float(input("Enter the student total marks: "))
        filename = input("Enter the filename: ")

        # Define the student's data as a list
        student_data = [st_id, st_name, st_marks]

        # Load existing data from the file if available, else create a new list
        students_data = []
        try:
            with open(filename, 'rb') as fp:
                students_data = pickle.load(fp)
        except (FileNotFoundError, EOFError):
            pass

        # Ensure that students_data is a list of lists
        if not isinstance(students_data, list):
            students_data = []

        # Append new student data to the existing list
        students_data.append(student_data)

        # Save updated list back to the file
        with open(filename, 'wb') as fp:
            pickle.dump(students_data, fp)

        print(f"Data stored in {filename} successfully")
        return students_data
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to display the student data in PrettyTable
def pretty_table(students_data):
    # Define column headers for the table
    columns = ['Student ID', 'Student Name', 'Student Marks']

    # Create a PrettyTable object
    my_table = PrettyTable()
    my_table.field_names = columns

    # Add each student's data as a row in the table
    for student in students_data:
        # Ensure each student entry is a list or tuple before adding to table
        if isinstance(student, list) or isinstance(student, tuple):
            my_table.add_row(student)

    # Display the table
    print(my_table)

# Function to retrieve and display all data from the file
def show_data():
    try:
        filename = input("Enter the filename: ")

        # Load data from the file
        with open(filename, 'rb') as fp:
            students_data = pickle.load(fp)

        # Check if there's any data to display and ensure it's a list of lists
        if students_data and isinstance(students_data, list):
            pretty_table(students_data)
        else:
            print("No valid data found!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
    except EOFError:
        print(f"{filename} is empty")

# Function to display the menu and handle user options
def menu():
    print("=" * 70)
    print("\t\t\tMENU")
    print("=" * 70)
    print("\t1. Insert student data")
    print("\t2. Show all student data")
    print("\t3. Exit")
    print("=" * 70)

    while True:
        choice = int(input("Choose the option from the menu: "))
        match(choice):
            case 1:
                insert_data()  # Insert and store data
            case 2:
                show_data()  # Retrieve and display all data in table
            case 3:
                exit()
            case _:
                print("Please choose a valid option from the menu.")

# Main program
menu()
