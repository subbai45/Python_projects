#to find the total digits in the list

def largestNumber(lst):
    cnt = 0
    for val in lst:
        while(val):
            val=val//10
            cnt += 1
    return cnt

#main program
lst=[]
i=0
print("="*50)
while True:
    var = input("Enter the {}th value(to stop press '!'): ".format(i))
    print("~" * 50)
    if(var=='!'):
        break
    lst.append(float(var))
    i += 1
res=largestNumber(lst)
print()
print("=" * 50)
print("list of given values are {}".format(lst))
print("="*50)
print("Total number of digit count is {}".format(res))
print("="*50)
