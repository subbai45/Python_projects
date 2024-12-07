# to store the list of prime numbers in a list

def isprime(n):
    i=2
    res=True
    while(i<n):
        if(n%i==0):
            res=False
            break
        i += 1
    return res
lst=[]
print("="*100)
num=int(input("Enter the Number: "))
if(num<2):
    print("Invalid Number, Please enter greater than two")
else:
    for i in range(2,num+1):
        res=isprime(i)
        if(res==True):
            lst.append(i)
print("="*100)
print("List of Prime Numbers under {} is {}".format(num,lst))
print("="*100)