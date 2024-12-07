# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

import input as inn

list_1=inn.input_list()
dummy_list=[]
final_list=list_1.copy()
print()
remove_elements=(int(val) for val in input("Enter the number of indexed value to be removed by space: ").split())
for val in remove_elements:
    dummy_list.append(list_1[val])
for val in dummy_list:
    final_list.remove(val)
print("original list of values are: ",list_1)
print("final list of elements are: ",final_list)
del dummy_list