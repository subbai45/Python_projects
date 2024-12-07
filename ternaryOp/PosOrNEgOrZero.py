#check whether the given number is positive or negative or zero

num=float(input("enter the Number: "))
res="Positive" if num>0 else "Negative" if num<0 else "Zero"
print("="*40)
print("\t{} is {}".format(num,res))
print("="*40)