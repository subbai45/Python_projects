# to print the palindrome triangle upto given range from 1 to 10

n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()