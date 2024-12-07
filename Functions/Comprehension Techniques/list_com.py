# to list the given values in the from of list by using list comprehension techniques

print("Enter the values with space: ")
list_values=[val for val in input().split()]
print(list_values)

print("-"*100)

print("Enter the values to find their square root: ")
square_root=[int(val)**2 for val in input().split()]
print(square_root)
for var in range(len(square_root)):
    print("{}--->{}".format(square_root[var],type(var)))