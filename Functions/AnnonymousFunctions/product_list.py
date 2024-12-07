# product the all elements of list ny using anonymous function along with the reduce function
import functools as fc
import numpy as np
lst = []
#lst = input("Enter the values by space: ").split()
n = int(input("Enter the length of the list: "))
for _ in range(0,n+1):
    val = np.random.randint(10, 15)
    lst.append(val)
# lst = input("Enter the list of values by giving space: ").split()
#lst = [float(val) for val in lst if val.isdigit()]
print(lst)
prod = lambda x,y:x*y
prod_lst = fc.reduce(prod,lst)

print(f"product of list {lst} is {prod_lst}")