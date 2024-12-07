#to find the temperature conversion calculator

menu="""===============================================
        Temperature Calculator
===============================================
        1. Farehnheit to Celsius
        2. Farehnheit to Kelvin
        3. Celsius to Farehnheit
        4. Celsius to Kelvin
        5. Kelvin to Celsius
        6. Kelvin to Farehnheit
        7. Exit
================================================"""
print(menu)
choice=int(input("Enter ur choice by seeing menu: "))
print("="*70)
match(choice):
    case 1:
        f = float(input("Enter the temperature of Farehnheit: "))
        c = (f-32)*(5/9)
        print("By converting Temperature from Farehnheit {} to Celsius is {}".format(f,c))
    case 2:
        f = float(input("Enter the temperature of Farehnheit: "))
        k = (f-32)*(5/9)+273.15
        print("By converting Temperature from Farehnheit {} to Kelvins is {}".format(f, k))
    case 3:
        c = float(input("Enter the temperature of Celsius: "))
        f = ((9/5)+32)
        print("By converting Temperature from Celsius {} to Farehnheit is {}".format(c,f))
    case 4:
        c = float(input("Enter the temperature of Celsius: "))
        k = c + 273.15
        print("By converting Temperature from Celsius {} to Kelvins is {}".format(c, k))
    case 5:
        k = float(input("Enter the temperature of Kelvins: "))
        c = k-273.15
        print("By converting Temperature from Kelvins {} to celsius is {}".format(k, c))
    case 6:
        k = float(input("Enter the temperature of Kelvins: "))
        f = (k-273.15)*(9/5)+32
        print("By converting Temperature from Kelvins {} to farehnheit is {}".format(k, f))
    case 7:exit()
    case _:
        print("Invalid input,Please enter valid input to perform operations")
print("-"*70)
print("Program execution completed")
print("="*70)