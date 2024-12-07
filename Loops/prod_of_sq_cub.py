#to display the product of squares and cubes of n natural numbers
import math
num=int(input("Enter the number: "))
sq,cb=1,1

print("="*60)
print("Squares\t\tCubes")
for i in range(1,num+1):
    print("\t{}\t\t{}".format(i**2,i**3))
    sq = sq * i ** 2
    cb = cb * i ** 3
else:
    print("="*60)
    print("\t{}\t\t{}".format(sq,cb))
    print("="*60)
i=1
print("Squares\t\tCubes")
print("-"*60)
cb,sq=1,1
while(i<=num):
    print("\t{}\t\t{}".format(i ** 2, i ** 3))
    cb = cb * i ** 3
    sq = sq * i ** 2
    i = i + 1

else:
    print("=" * 60)
    print("\t{}\t\t{}".format(sq, cb))
    print("=" * 60)
