#to find the maximum and minimum in the list of values

lst=[]
i=0
print("="*60)
while(1):
    var=input("Enter the {}th value (to stop press '!'): ")
    print("-" * 60)
    i += 1
    if(var=='!'):
        break
    lst.append(float(var))
print()
max=min=lst[0]
st=set(lst)
if(len(st)==1):
    print("All values are equal {}".format(lst))
else:
    for val in lst:
        if(max<val):
            max=val
        elif(min>val):
            min=val
    else:
        print()
        print("=" * 60)
        print("Maximum value from the list is {}".format(max))
        print("-" * 60)
        print("Minimum value from the list is {}".format(min))
        print("=" * 60)