# Create a Person class with attributes for name and age. Add a method called display_info() that prints these details
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("="*50)
        for val,var in self.__dict__.items():
            print(f"{val} --> {var}")
        print("="*50)


# Main Program
name = input("Enter the person name: ").title()
age = int(input("Enter the person age: "))
per = person(name,age)
per.display()


