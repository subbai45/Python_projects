# Find Intersection of Two Lists:
# Use a lambda function with filter to find the intersection of two lists (i.e., elements that are common in both lists).

lst1 = input("Enter the list-1 values: ").split()
lst2 = input("Enter the list-2 values: ").split()

common_list= []

common = lambda val1: val1 in lst1
common_list = list(filter(common,lst2))
print("common in the both list are: ",common_list)
