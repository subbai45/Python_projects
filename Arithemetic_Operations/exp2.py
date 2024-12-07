#calculate the expression of (a^m)/(a^n)

a=float(input("enter the value of 'a': "))
m=float(input("enter the value of 'm': "))
n=float(input("enter the value of 'n': "))

#exp=(a**m)/(a**n)
exp=(a)**(m-n)
print("="*50)
print("the value of the expression is {}".format(exp))
print("="*50)