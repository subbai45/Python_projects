#program to display the sum of the list

def sumof(lst):
	sum=0
	for val in lst:
		sum+=val
	return sum

#main program
lst=[]
i=0
print("="*50)
while True:
	var=input("Enter the {}th value(TO stop press '!'): ".format(i))
	print("~"*50)
	if(var == '!'):
		break
	lst.append(float(var))
	i += 1
res=sumof(lst)
print("="*50)
print("list of values are {}".format(lst))
print("="*50)
print("Sum of list is {}".format(res))