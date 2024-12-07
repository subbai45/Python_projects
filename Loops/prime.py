# to find the prime number of given input

num=int(input("Enter the Number: "))
i=2
print("="*30)
if(num<2):
    print('Invalid Input, Enter above two')
res=True
while(i<num):
    if(num%i==0):
        res=False
        break
    i+=1
if(res==True):
    print("\t{} is a Prime Number".format(num))
else:
    print("\t{} is Not a Prime Number".format(num))
print("="*30)