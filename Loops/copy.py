# to know about shallow and deep copy
lst = ['rohit','kohli','pant']
lst1 = lst.copy() # shallow copy
lst1[2]='shirley'
print("="*50)
print("\t\t\tShallow COpy")
print("="*50)
print(f"{lst} --> {id(lst)}")
print("-"*50)
print(f"{lst1} --> {id(lst1)}")
print("="*50)
lst2 = ['sunday','monday','tuesday']
lst3 = lst2 # deep copy
lst3[1] = 'Saturday'
print("\t\t\t Deep Copy")
print("="*50)
print(f"{lst2} --> {id(lst2)}")
print("-"*50)
print(f"{lst3} --> {id(lst3)}")
print("="*50)
print()


