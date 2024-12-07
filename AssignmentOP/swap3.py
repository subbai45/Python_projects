#swapping of two numbers

a=float(input("enter the first value(except 'str') : "))
b=float(input("enter the second value(except 'str') : "))

print("="*30)
print("\tSWAPPING TWO NUMBERS")
print("="*30)
print("\tbefore swapping a = {}".format(a))
print("\tbefore swapping b = {}".format(b))
print("-"*30)
a=a*b  #swapping using multiline assignment operator
b=a/b
a=a/b
print("\tafter swapping a = {}".format(a))
print("\tafter swapping b = %0.1f" %b)
print("="*30)