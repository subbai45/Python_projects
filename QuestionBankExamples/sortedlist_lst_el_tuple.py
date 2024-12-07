# 6.Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# main program
sample_list=[]
range_of_list=int(input("Enter the range of the list: "))

for i in range(range_of_list):

    value_1=int(input("Enter the first element: "))
    value_2=int(input("Enter the second element: "))
    sample_list.append((value_1,value_2))
print()
sample_list.sort(key=lambda val:val[1])
print(sample_list)