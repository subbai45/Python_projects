#find whether the given number is even or odd

num=float(input("Enter the number: "))
res="Even" if num%2==0 else "Odd"

print("="*30)
print("\t{} is {}".format(num,res))
print("="*30)