# to print the list of prime numbers of given values of the list by using filter()

def isprime(n):
    res = True
    i=2
    while i < n:
        if (n % i == 0):
            res = False
            break
        i += 1
    return res
prime = lambda val:isprime(val) # Annonymous Function

#main program
lst=[]
i=0
while True:
    val = input("Enter the {}th value (To stop press '!'): ".format(i))
    if val == '!':
        break
    if val.isalpha():
        continue
    elif val.isspace():
        continue
    elif val.isdigit():
        lst.append(float(val))
    i += 1

prime_list=list(filter(prime,lst))
print()
print("Original List: ",lst)
print()
print("Prime list: ",prime_list)