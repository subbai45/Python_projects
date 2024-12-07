# to find the index of the specific element of the list
print("Enter the list values: ")
lst=list(val for val in input().split())
index=int(input("Enter the index number,to know the element: "))
print(f"list of values are {lst},Length of list is {len(lst)}")
if index in range(0,len(lst)):
    val=lst[index]
    print("retrived val from the list is: ",val)
else:
    print("Invalid Index")