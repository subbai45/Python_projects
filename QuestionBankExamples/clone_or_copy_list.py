# 9. Write a Python program to clone or copy a list.

def clone(lst):
    lst1=[]
    lst2=lst.copy()
    lst1=lst
    return lst1,lst2

#main program
lst=[]
i=0
while True:
    val=input("Enter the {}th values(Press ! to stop): ".format(i))
    if(val == '!'):
        break
    lst.append(val)
    i += 1
print()
res=clone(lst) # function call
# print(res)
print("="*50)
print("Original list:",lst,id(lst))
print("~"*50)
print("Deep copy:",res[0],id(res[0]))
print("~"*50)
print("Shallow Copy:",res[1],id(res[1]))
print("="*50)
# print(res[1][2:4])