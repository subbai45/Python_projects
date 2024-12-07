#swapping of two numbers

a=input("Enter First value: ")
b=input("enter the Second value: ")
print("="*35)
print("\tSWAPPING TWO VAALUES")
print("="*35)
print("\tbefore swapping a = {}".format(a))
print("\tbefore swapping b = {}".format(b))
print("-"*35)
a,b=b,a    #swapping using multiline assignment operator
print("\tafter swapping a = {}".format(a))
print("\tafter swapping b = {}".format(b))
print("="*35)