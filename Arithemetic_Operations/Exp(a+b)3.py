#to evaluate the expression of (a+b)3
#formula for (a+b)3 is \(a^{3}+3a^{2}b+3ab^{2}+b^{3}\)

a=float(input("Enter the first number: "))
b=float(input("enter the second number: "))
#exp=(a+b)**3
exp=a**3+3*a**2*b+3*a*b**2+b**3
#exp=(a+b)*(a+b)*(a+b)
print("="*40)
print("(a+b)3 Expresion result is {}".format(exp))
print("="*40)