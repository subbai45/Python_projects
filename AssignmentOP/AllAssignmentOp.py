#All Assignment operators using multiline assignment operations

a=float(input("Enter the first value: "))
b=float(input("Enter the second value: "))
sum,sub,mul,ndiv,fdiv,mod,exp=a+b,a-b,a*b,a/b,a//b,a%b,a**b

print("="*60)
print("All Assignment Operators")
print("="*60)
print("Sum of {} + {} = {} ".format(a,b,sum))
print("Sub of {} - {} = {} ".format(a,b,sub))
print("Mul of {} x {} = {} ".format(a,b,mul))
print("Normal Division of {} / {} = {} ".format(a,b,ndiv))
print("Floor Division of {} // {} = {} ".format(a,b,int(fdiv))
print("Modulo Division of {} % {} = {} ".format(a,b,mod))
print("="*60)
