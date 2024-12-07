#3. Write a Python program to get the Maximum and Minimum number from a list.


def max(lst):
	max=lst[0]
	for i in range(0,len(lst)):
		if(max < lst[i]):
			max=lst[i]
	return max
def min(lst):
	min=lst[0]
	for i in range(0,len(lst)):
		if(min > lst[i]):
			min=lst[i]
	return min
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
max = max(lst)
min = min(lst)
print()#to look spacious
print("="*50)
print("list of values are {}".format(lst))
print("="*50)
print("Max value from the list is {}".format(max))
print("~"*50)
print("Min value from the list is {}".format(min))
print("="*50)