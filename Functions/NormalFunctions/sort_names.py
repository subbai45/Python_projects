#to sort the list of str data or names and sort it in ascending as well as descending order

def readvalues():
    i = 0
    lst=[]
    print("=" * 50)
    while True:
        val = input("Enter the {}th Name(press '!' to stop): ".format(i))
        print("~" * 50)
        if (val == '!'):
            break
        lst.append(val)
        i += 1
    return lst
def sortof(lst_names):
    if(len(lst_names)==0):
        print("Empty list, could not sort the empty list")
        print('=' * 100)
    else:
        #dsc= list_names.sort()[::-1]
        print("Ascending order list-->{}".format(sorted(lst_names)))
        print('~'*100)
        print("Decending order-->{}".format(sorted(lst_names)[::-1]))
        print("="*100)

#main Program
lst_names=readvalues()
print()
print("Original list -->",lst_names)
print('='*100)
sortof(lst_names)
