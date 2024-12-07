#to find the biggest number from the two numerical inputs

def maxtwo(a,b):
    if(a>b):
        print("{} is biggest number among {} and {}".format(a,a,b))
    elif(a<b):
        print("{} is biggest number among {} and {}".format(b,a,b))
    else:
        print("Both are equal {} and {}".format(a,b))
    print("=" * 60)

print("="*60)
num1=float(input("Enter the First number: "))
print("-"*60)
num2=float(input("Enter the second number: "))
print("="*60)

maxtwo(num1,num2)