# to find the maximum nd minimum values of the list

max_value=lambda maxv:max(maxv)
min_value=lambda minv:min(minv)

#main program

lst=[]
print("="*60)
print("Enter the values separated with space: ")
lst=[float(val) for val in input().split()]
res=max_value(lst)
res1=min_value(lst)
print("="*60)
print("list of values are ",lst)
print("="*60)
print("Maximum of given list is ",res)
print("~"*60)
print("Minimum of given list is ",res1)
print("="*60)