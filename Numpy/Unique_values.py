# to print the unique values as well as its frequency

import numpy as np
arr = np.random.randint(0,40,(3,3))
print("array: \n",arr)
arr_unique,arr_index,arr_count = np.unique(arr,return_index=True,return_counts=True)
print(arr_unique,"\n",arr_index,'\n',arr_count)

print("-"*60)
arr = np.random.randint(0,45,20)
print(arr,type(arr))
arr = sorted(arr)
lst={}
for val in arr:
    if val not in lst:
        lst[val]=1
    else:
        lst[val]=lst.get(val)+1
print(lst)