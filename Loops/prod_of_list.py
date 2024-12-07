#to product the list of numbers

lst=[]
i=0
print("-"*70)
while(1):
    var=input("Enter the {}th value (to stop press '!'): ".format(i))
    print("-" * 70)
    i += 1
    if(var=='!'):
        break
    lst.append(float(var))
print()
prod=1
for val in lst:
    prod *= val
print("="*70)
print("product of list of numbers({}) is {}".format(lst,prod))
print("="*70)