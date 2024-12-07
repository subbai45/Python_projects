# TO take list of values dynamically and get prime numbers from list

lst=[]
lst1=[]
def isprime(n):
    res = True
    i=2
    while i < n:
        if (n % i == 0):
            res = False
            break
        i += 1
    return res
a=0
print("="*60)
while True:
    i=input("Enter the {}th value(To stop press'!'): ".format(a))
    print("~"*60)
    if(i=='!'):
        break
    lst.append(int(i))
    a += 1
print("list of values {}".format(lst))
print("~"*60)
for val in lst:
    if val < 2:
        continue
    if(isprime(val)==True):
        lst1.append(val)
print("list of prime numbers from the given list are {}->{}".format(len(lst1),lst1))
print("="*60)