#to find the biggest number among the given inputs

num1=float(input("Enter the num1: "))
num2=float(input("Enter the num2: "))
num3=float(input("Enter the num3: "))

print("="*40)
if(num1>num2) and (num1>num3):
    print("Biggest of ({},{},{}) is {}".format(num1,num2,num3,num1))
if(num2>num1) and (num2>num3):
    print("Biggest of ({},{},{}) is {}".format(num1,num2,num3,num2))
if(num3>num2) and (num3>num1):
    print("Biggest of ({},{},{}) is {}".format(num1,num2,num3,num3))
if(num1==num2) and (num2==num3) and (num3==num1):
    print("All the Numbers are Equal")
print("="*40)