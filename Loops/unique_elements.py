# to print only unique elements out of given list of values without using set() typecasting
lst=[]
i=0
print("="*50)
while True:
    var=input("Enter the {}th value (To stop press '!'): ".format(i))
    print("-" * 50)
    i += 1
    if(var=='!'):
        break
    lst.append(float(var))
lst1=[]
for val in lst:
    if val not in lst1:
        lst1.append(val)
print("="*50)
print("list of values ",lst)
print("-"*50)
print("list of unique values ",lst1)
print("="*50)
