# to calculate the sum and average of the given infinite list

lst=[]
i=0
sum,avg=0,0
print("="*60)
while(1):
    var=input("Enter the {}th value of list( to stop enter '!'): ".format(i))
    i+=1
    if(var=='!'):
        break
    lst.append(float(var))
    sum=sum+float(var)
print()
print("="*100)
print("Sum of the given list {} is '{}'".format(lst,round(sum,2))) #sum() we can use sum() general function to sum list of values
print("-"*100)
print("Avg of the given list {} is '{}'".format(lst,round(sum/len(lst),2)))
print("-"*100)
print("Length of the list is ",len(lst))
print("="*100)