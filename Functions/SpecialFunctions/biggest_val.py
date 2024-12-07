# to find the biggest values among the list of values by using reduce()
from functools import reduce


'''def max_val(k,v):
    if k>v:
        return k
    else:
        return v'''
list_1=[]
i=0
while True:
    var=input(f"Enter the {i}th value of list-1(To stop press '!'): ")
    if var == '!':
        break
    list_1.append(float(var))
    i += 1
print()
#biggest_val=reduce(max_val,list_1)
biggest_val=reduce(lambda k,v:k if k>v else v,list_1)
smallest_val=reduce(lambda k,v:k if k<v else v,list_1)
print("="*100)
print(f"Biggest value from the list of {list_1} is {biggest_val}")
print("="*100)
print(f"Smallest value from the list of {list_1} is {smallest_val}")
print("="*100)