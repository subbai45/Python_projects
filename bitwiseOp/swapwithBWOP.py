#swapping two integer by using bitwise operators

a,b=int(input('Enter the First number: ')),int(input('Enter the second Number: '))
print("="*40)
print("before swapping a is {}".format(a))
print("before swapping b is {}".format(b))
print("-"*40)
a=a^b
b=a^b
a=a^b
print("after swapping a is {}".format(a))
print("after swapping b is {}".format(b))
print("="*40)