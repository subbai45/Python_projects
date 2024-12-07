# to display the multiples of 5 within 'n'
n = int(input("Enter the number: "))
i = 1
if n < 5:
    print("Enter the number greater than or equal to '5'")
else:
    while i <= n:
        if i % 5 == 0:
            print(i, end=" ")
        i += 1
