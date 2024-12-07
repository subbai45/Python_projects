# Entire name validation with regular expressions

import re
def name_validation(name):
    try:
        valid_name = re.search(r'^[A-Z][a-z]+( [A-Z][a-z]+)*$',name.title())
        if valid_name != None:
            return valid_name.group()
        else:
            print(f"{name} is Not a Valid Name")
    except (ValueError or TypeError):
        print("Something went wrong! please check ur code")


# Main Program
while True:
    name = input("Enter the Name: ")
    valid = name_validation(name)
    if valid != None:
        print("Valid Name: ",valid)
        break
    else:
        print(f"\t\t{name} is not valid, Please enter name again!")