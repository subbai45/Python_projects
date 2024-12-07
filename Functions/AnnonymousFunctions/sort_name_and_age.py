# custom sort the age and name

dic = {}
lst = []
n = int(input("Enter the number of entries: "))
for val in range(n):
    name = input("Enter the name: ")
    age = int(input(f"Enter the age: "))
    lst.append({'name':name,'age':age})

# main program
sorted_lst = sorted(lst,key=lambda val:(val['age'],val['name']))

print(lst)
print(sorted_lst)
