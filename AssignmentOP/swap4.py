#swapping of two numbers

a=input("Enter First value: ")
b=input("enter the Second value: ")
print("="*35)
print("\tSWAPPING TWO VALUES")
print("="*35)
print("\tbefore swapping a = {}".format(a))
print("\tbefore swapping b = {}".format(b))
print("-"*35)
temp=a   #swapping using multiline assignment operator
a=b
b=temp

print("\tafter swapping a = {}".format(a))
print("\tafter swapping b = {}".format(b))
print("="*35)