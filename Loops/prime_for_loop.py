#to display the prime number by using for loop

num=int(input("Enter the Number: "))
res=True
print("="*33)
for i in range(2,num):
    if(num%i==0):
        res=False
        break
if(res==True):
    print("\t{} is a Prime Number".format(num))
else:
    print("\t{} is Not a Prime NUmber".format(num))
print("="*33)