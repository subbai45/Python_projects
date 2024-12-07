# to know whether the given number is float or not
print("="*50)
flt=input("Enter the number: ")
print("="*50)
cnt=0
for i in flt:
    if(i=='.'):
        cnt=cnt+1
    if(not i.isnumeric()):
        break
if(cnt==1):
    print("\t{} Float number".format(float(flt)))
elif(flt.isalpha()):
    print("\t'{}' Not a Number,Dont enter alpha".format(flt))
else:
    print("\t{} is Not a Float Number".format(flt))
print("="*50)