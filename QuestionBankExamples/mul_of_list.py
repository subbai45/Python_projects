#program to display the mul all the values in the list

def mulof(lst):
	mul=1
	for val in lst:
		mul *= val
	return mul

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
res = mulof(lst)
print("="*50)
print("list of values are {}".format(lst))
print("="*50)
print("product of the list is {}".format(res))
print("="*50)