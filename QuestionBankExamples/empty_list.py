# 8. Write a Python program to check a list is empty or not.
lst=[]
i=0
while True:
    val=input("Enter the {}th values(Press ! to stop): ".format(i))
    if(val == '!'):
        break
    lst.append(val)
    i += 1
print()
print("="*50)
if(len(lst) > 0):
    print("given list is not empty {}".format(lst))
else:
    print("Empty list {}".format(lst))
print("="*50)

