#to find the whether the given number is positive or negative

num=float(input("Enter the Number: "))
print("="*30)
if(num>0):
    print("{} is Positive".format(num))
elif(num<0):
    print("{} is Negative".format(num))
else:
    print("{} is Zero".format(num))
print("="*30)