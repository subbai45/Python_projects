#to impliment the calculator by using match_case statements
menu="""===============================================
        Arithemetic Calculator
===============================================
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division and (Floor Division)
        5. Exponential
        6. Exit
================================================"""
print(menu)
choice=int(input("Enter your choice for calculation: "))
print("="*60)
match(choice):
    case 1:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("\n")
        print("Sum of {} and {} is {}".format(a, b, a+b))
    case 2:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("\n")
        print("Sub of {} and {} is {}".format(a, b, a-b))
    case 3:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("\n")
        print("Mul of {} and {} is {}".format(a, b, a*b))
    case 4:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("\n")
        print("Normal Division of {} and {} is {}".format(a, b, a/b))
        print("Floor Division of {} and {} is {}".format(a, b, a // b))
    case 5:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("\n")
        print("Exponentation of {} and {} is {}".format(a, b, a**b))
    case 6:exit()
    case _:
        print("you entered invalid input,please enter the valid input")
print("-" * 60)
print("Program exection completed")
print("="*60)