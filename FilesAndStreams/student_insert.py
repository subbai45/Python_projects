# inserting the data dynamically by using pickle module
import pickle
from prettytable import PrettyTable
def insert_data():
    while True:
        try:
            st_id = int(input("Enter the student i'd: "))
            st_name = input("Enter the student name: ").upper()
            st_marks = float(input("Enter the student total marks: "))
            global filename
            filename = input("Enter the filename: ")
            student_columns = ['st_id', 'st_name', 'st_marks']
            student_data = [st_id,st_name,st_marks]
            try:
                with open(filename,'rb') as rp:
                    students_data = pickle.load(rp)
            except (FileExistsError,EOFError):
                print("Enter valid filename")
            students_data.append(student_data)
            with open (filename,'ab') as fp:
                pickle.dump(students_data,fp)
                print(f"Data stored in {filename} successfully")
            return students_data,student_columns
        except FileNotFoundError:
            print(f"{filename} Does not exist")
        except FileExistsError:
            print(f"{filename} already exist")

def show_data():
    try:
        filename = input("Enter the filename: ")
        with open(filename,'rb') as fp:
            file_data = pickle.load(fp)
            print(file_data)
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
def pretty_table(students_data,student_columns):
    my_table = PrettyTable(student_columns)
    for data in students_data:
        my_table.add_row(data)



def menu():
    print("="*70)
    print("\t\t\tMENU")
    print("="*70)
    print("\t1.Insert students data")
    print("\t2.Show students data")
    print("\t3.Enter data in table")
    print("\t4.Exit")
    print("="*70)
    student_columns = []
    studens_data = []
    while True:
        try:
            choice = int(input("Choose the option from the menu: "))
            match(choice):
                case 1:
                   insert_data()
                case 2:
                    show_data()
                case 3:
                    if student_columns and studens_data:
                        pretty_table(student_columns,studens_data)
                case 4:exit()
                case _:
                    print("Please choose the valid input from the menu")
        except ValueError:
            print("Please Enter only digits from the menu")


# Main program
students_data = []

menu()


