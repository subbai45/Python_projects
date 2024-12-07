# 11. Write a Python function that takes two lists and returns True if they have at least one
# common member

import input
common_list=[]
list_1=input.input_list()
list_2=input.input_list()
res = False
cnt=0
for val in list_1:
    if val in list_2:
        common_list.append(val)
        cnt += 1
        res = True
print()
print("First list: ",list_1)
print("Second list: ",list_2)
print()
if res == True:
    print("In the both list there are {} common elements: {}".format(cnt,common_list))
elif len(list_1) & len(list_2) == 0:
    print("Invlaid List,list should not be empty")
else:
    print('='*30)
    print("\tBoth are unique lists")
    print('=' * 30)