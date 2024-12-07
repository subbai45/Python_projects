# to find the sum and avg of the give list of values

def readvalues(lst):
    i=0
    print("="*50)
    while True:
        val = input("Enter the {}th value(press '!' to stop): ".format(i))
        print("~" * 50)
        if(val=='!'):
            break
        lst.append(float(val))
        i += 1
    return lst
def sumof(list_values):
    sum=0
    for i in list_values:
        sum+=i
    return sum
def avgof(sum,len):
    avg=sum/len
    return avg
#main program
lst=[]
list_values=readvalues(lst)

sum=sumof(list_values)
print("="*100)
print("Sum of {} is {}".format(list_values,sum))
avg=avgof(sum,len(list_values))
print("~"*100)
print("Average of {} is {}".format(list_values,avg))
print("="*100)