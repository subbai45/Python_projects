# to print the sum of squares and sum of cubes of 'n' natural numbers

num = int(input("Enter the number: "))
if (num <= 0):
    print("Invalid input, Enter only Positive inputs of integers")
else:
    i = 1
    sum = 0
    while(i <= num):
        sum = sum + i ** 2 # or sum += i**2 (here, i**2 for square)
        i = i + 1 # or i += 1
    else:
        print("="*60)
        print("the Sum of Square natural numbers from 1 to {} is {} ".format(num,sum))
        print("-" * 60)
sum = 0
for var in range(1, num + 1):
    sum = sum + var ** 3
else:
    print("the Sum of Cube natural numbers from 1 to {} is {} ".format(num, sum))
    print("=" * 60)
