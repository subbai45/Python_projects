#to display the product of n natural numbers i.e., 1*2*3*4*5.....

num=int(input("Enter the number: "))
i=1
prod=1
print("="*60)
if(num<=0):
    print("Invalid input, please enter only positive integers")
else:
    while(i<=num):
        prod=prod*i
        i=i+1
    else:
        print("The product of given natural numbers from 1 to {} is {}".format(num,prod))
        print("Also we can say {}! is {}".format(num,prod))
print("-"*60)
import math as f
fact=f.factorial(num)
print("{}! is {}".format(num,fact))
print("="*60)