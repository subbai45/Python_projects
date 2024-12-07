import json

# File to store student data
DATA_FILE = 'students_data.json'


# Function to load data from JSON file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Function to save data to JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


# Student Management System
class StudentManagementSystem:

    def __init__(self):
        self.students = load_data()

    def add_student(self, name, marks):
        if name in self.students:
            print(f"Student '{name}' already exists.")
        else:
            self.students[name] = marks
            save_data(self.students)
            print(f"Student '{name}' added successfully.")

    def update_student(self, name, marks):
        if name in self.students:
            self.students[name] = marks
            save_data(self.students)
            print(f"Student '{name}' updated successfully.")
        else:
            print(f"Student '{name}' not found.")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            save_data(self.students)
            print(f"Student '{name}' deleted successfully.")
        else:
            print(f"Student '{name}' not found.")

    def display_students(self):
        if not self.students:
            print("No student records found.")
        else:
            print("Student Records:")
            for name, marks in self.students.items():
                print(f"Name: {name}, Marks: {marks}")


# Menu function for interacting with the system
def menu():
    system = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student Marks")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            marks = input("Enter student's marks: ")
            system.add_student(name, marks)

        elif choice == '2':
            name = input("Enter student's name: ")
            marks = input("Enter new marks: ")
            system.update_student(name, marks)

        elif choice == '3':
            name = input("Enter student's name: ")
            system.delete_student(name)

        elif choice == '4':
            system.display_students()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select a valid option.")


# Run the system
if __name__ == '__main__':
    menu()
