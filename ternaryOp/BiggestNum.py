#check whether the given is biggest among of another number

num1=float(input("Enter the first Number: "))
num2=float(input("Enter the second Number: "))
res= num1 if num1>num2 else num2 if num2>num1 else "Both are Equal"
print("="*52)
print("\t Among({},{}) {} ".format(num1,num2,res))
print("="*52)