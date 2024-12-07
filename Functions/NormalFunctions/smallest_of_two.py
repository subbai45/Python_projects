#to find the Smallest number from the two numerical inputs

def maxtwo(a,b):
    if(a<b):
        return a
    elif(a>b):
        return b
    else:
        print("Both are equal {} and {}".format(a,b))

print("="*60)
num1=float(input("Enter the First number: "))
print("-"*60)
num2=float(input("Enter the second number: "))
print("="*60)

res=maxtwo(num1,num2)
if res!=None:
    print("{} is smallest number among {} and {}".format(res, num1, num2))
print("="*60)