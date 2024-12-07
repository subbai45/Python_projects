# To print the sum of list of numerical values

lst=[]
print("="*50)
num=int(input("Enter how many numbers you want to append in empty list: "))
print("="*50)
if(num<=0):
    print("{} is Invalid Input".format(num))
for i in range(num):
    lst.append(float(input("\tEnter the {}th value: ".format(i))))
else:
    print("-"*50)
    print("list of Elements: ",lst)
sum=0
for var in lst:
    sum=sum+var
else:
    print("=" * 50)
    print("The Sum of values in list is {}".format(sum))
    print("=" * 50)