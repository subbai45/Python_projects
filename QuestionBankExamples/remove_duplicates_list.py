# 7. Write a Python program to remove duplicates from a list.

def duplicates(lst):
    lst_dup = []
    for val in lst:
        if val not in lst_dup:
            lst_dup.append(val)
    return lst_dup,len(lst_dup)
# Main Program

lst=[]
i=0
print("="*100)
while True:
    var=input("Enter the {}th value (To stop press '!'): ".format(i))
    print("~" * 100)
    if(var == '!'):
        break
    lst.append(var)
    i += 1
print()
print("="*100)
print("Before Duplicates removed",lst)
lst=duplicates(lst)
print("~"*100)
#lst=set(lst) removing duplicates by using set() typecasting method
print("After duplicates removed",lst)
print("="*100)