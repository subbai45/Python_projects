#to find the perimeter of all the angles

menu="""===============================================
        Perimeter Calculator
===============================================
        T. TRIANGLE
        S. SQUARE
        R. RECTANGLE
        C. CIRCLE
        P. PARALLELOGRAM
        E. EXIT
================================================"""
print(menu)
choice=input("Enter your choice by seeing Menu: ")#.upper()
print("="*70)
match(choice.upper()):
    case 'T':#case 'T' | 't'
        print("PERIMETER OF TRIANGLE")
        a = float(input("Enter the length of 'a' value: "))
        b = float(input("Enter the length of 'b' value: "))
        c = float(input("Enter the length of 'c' value: "))
        perimeter = a+b+c
        print("Perimeter of Triangle for given values({},{},{}) is {}cm".format(a,b,c,perimeter))
    case 'S':#case 'S' | 's'
        print("PERIMETER OF SQUARE")
        side = float(input("Enter the length of any side of Square: "))
        perimeter = 4*side
        print("Perimeter of Square for given side({}) is {}cm".format(side, perimeter))
    case 'R':#case 'R' | 'r'
        print("PERIMETER OF RECTANGLE")
        b = float(input("Enter the length of breadth: "))
        h = float(input("Enter the length of height: "))
        perimeter = 2*(b+h)
        print("Perimeter of Rectangle for given values({},{}) is {}cm".format(b,h, perimeter))
    case 'C':#case 'C' | 'c'
        print("PERIMETER OF CIRCLE")
        r = float(input("Enter the radius of circle: "))
        perimeter = 2*3.14*r
        print("Perimeter of Circle for given Radius({}) is {}cm".format(r, perimeter))
    case 'P':#case 'P' | 'p'
        print("PERIMETER OF PARALLELOGRAM")
        a = float(input("Enter the length of 'a' value: "))
        b = float(input("Enter the length of 'b' value: "))
        perimeter = 2*(a+b)
        print("Perimeter of Parallelogram for given values({},{}) is {}cm".format(a, b, perimeter))
    case 'E':exit()  #case 'E
    # ' | 'e'
    case _:
        print("Invalid input,please enter valid input to perform operation")
print("-"*70)
print("program execution completted")
print("="*70)