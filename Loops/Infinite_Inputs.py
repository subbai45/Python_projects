# to take list of inputs infinitely unitil providing specific value to stop the taking inputs

lst=[]
i=0
while(1):
    var=input("Enter the {}th value (to stop press !): ".format(i))
    i=i+1
    if(var=='!'):
        break
    lst.append(float(var))
print()
print("="*50)
print("list of values are ",lst)
print("-"*50)
print("Length of lst is ",len(lst))
print("="*50)


