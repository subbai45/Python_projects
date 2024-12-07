# 5. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def strrev(val):
    cnt=0
    lst_rev=[]
    for val in lst_elements:
        if (len(val) >= 2):
            if(val[0] == val[-1]):
                lst_rev.append(val)
                cnt += 1
    print("=" * 100)
    print("First and last letter same words are: ",lst_rev)
    print("=" * 100)
    return cnt


#Main Program

lst_elements=[]
i=0
print("="*100)
while True:
    var=input("Enter the {}th Elements(To stop press '!'): ".format(i))
    print("~" * 100)
    if(var=='!'):
        break
    lst_elements.append(var)
    i+=1
print()
res=strrev(lst_elements)
print("count of same first and last letter is ",res)
print("="*100)