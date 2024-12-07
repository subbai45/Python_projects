#To find the biggest number among 3 givrn inputs by using python ternary(if...else) operator

num1=float(input("Enter the num1: "))
num2=float(input("Enter the num2: "))
num3=float(input("Enter the num3: "))

res=num1 if (num1>num2) and (num1>num3) else num2 if (num2>num3) and (num2>num1) else num3 if (num3>num2) and (num3>num1) else "All are equal"

print("="*(len(str(res))+(30)))
print("Biggest of({},{},{}) is {}".format(num1,num2,num3,res))
print("="*(len(str(res))+(30)))