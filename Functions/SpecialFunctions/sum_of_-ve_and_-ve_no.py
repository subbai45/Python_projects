# to print the sum of positive and negative numbers separately by using special functions
pos_lst=lambda k:True if k>0 else False
neg_lst=lambda k:True if k<0 else False

print("Enter the values by giving space: ")
lst=list(int(val) for val in input().split())

positive_list=sum(list(filter(pos_lst,lst)))
negative_list=sum(list(filter(neg_lst,lst)))

print(f"sum of positive list is {positive_list}")
print()
print(f"sum of negative list is {negative_list}")