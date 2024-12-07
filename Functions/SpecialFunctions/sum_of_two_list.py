# to print the sum of un-equal length of two list in the another list by using the map()

#Main Program
list_1=[]
list_2=[]
i=0
while True:
    var=input(f"Enter the {i}th value of list-1(To stop press '!'): ")
    if var == '!':
        break
    list_1.append(float(var))
    i += 1
print("-"*80)
j=0
while True:
    var=input(f"Enter the {j}th value of list-2(To stop press '!'): ")
    if var == '!':
        break
    list_2.append(float(var))
    j += 1
print("-"*80)

if len(list_1)>len(list_2):
    for k in range(len(list_1)-len(list_2)):
        list_2.append(0)
elif len(list_2)>len(list_1):
    for k in range(len(list_2)-len(list_1)):
        list_1.append(0)
print()
print(list_1,'and',list_2)
print()
sum_list=list(map(lambda k,v: k+v ,list_1,list_2))
print("="*100)
print(sum_list)
print("="*100)

for v1,v2,v3 in zip(list_1,list_2,sum_list):
    print(f"{v1} + {v2} = {v3}")