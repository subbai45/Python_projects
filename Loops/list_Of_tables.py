# to print the multiplication table of given list

lst=[]
print("="*40)
num=int(input("Enter the length of list: "))
print("="*40)
for i in range(num):
    lst.append(int(input("Enter the {}th value to add into list: ".format(i))))
    print("-" * 40)
print("list of given inputs are {}".format(lst))
print("="*40)
for i in lst:
    j = 1
    while (j <= 10):
        print("\t|\t\t{} x {} = {}\t\t|".format(i, j, i * j))
        j += 1
    print("=" * 40)