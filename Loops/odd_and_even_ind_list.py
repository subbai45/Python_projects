#to find and sum the odd and even indices values of given list

lst=[]
print("="*50)
num=int(input("Enter the number of values u want to add in list: "))
print("="*50)
if(num<=0):
    print("invalid input,enter greater than 1")
for val in range(0,num):
    lst.append(int(input("Enter the {}th value: ".format(val))))
i=0
oddsum,evensum=0,0
print("="*50)
while(i<len(lst)):
    if(i%2==0):
        evensum += lst[i]
        i += 1
    else:
        if(len(lst)!=i):
            oddsum += lst[i]
            i += 1
for i in range(0,num):
    if(i%2==0):
        ev=lst[i]
        print("\t{}\t\t\t".format(ev))
    else:
        od=lst[i]
        print("\t\t\t\t{}".format(od))
print("="*50)
print("\t{}\t\t\t{}".format(evensum,oddsum))
print("="*50)