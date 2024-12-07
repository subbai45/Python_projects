#to print the square root of the integer value
print("Enter the numerical values by space to find their square roots: ")
lst=input().split()
square_root=[float(val)**2 for val in lst]
for var in range(len(square_root)):
    print("{}--->{}".format(lst[var],square_root[var]))

print("-"*100)

print("Enter the numerical values by space to find the square roots: ")
lst1=input().split()
type_cating=[float(val) for val in lst1]
sq_rt={var:var**2 for var in type_cating}
for value,root in sq_rt.items():
    print("{}--->{}".format(value,root))

