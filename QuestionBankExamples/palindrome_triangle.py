# to print the palindrome triangle to given range upto 1 to 10

for i in range(1, int(input("Enter the number of rows: "))+1):
    print((10 ** i - 1) ** 2 // 81)
print("-" * 100)
for i in range(1, int(input("Enter the number of rows: "))+1):
    print(((10 ** i - 1) // 9) ** 2)
