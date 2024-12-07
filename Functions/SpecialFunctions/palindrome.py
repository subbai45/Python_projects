# to print collect the list of palindromes in the list by using filter()

palindrome = lambda pal:True if pal == pal[::-1] else False

# Main Program
lst=[]
i=0
while True:
    val = input("Enter the {}th value (To stop press '!'): ".format(i))
    if val == '!':
        break
    lst.append(val)
    i += 1
print()
final_list=list(filter(palindrome,lst))
"""for var in lst:
    if(palindrome(var) == True):
        final_list.append(var)"""
print()
print("Original list",lst)
print()
print("Palindrome list",final_list)