#to display the number in reverse
print("="*40)
num=int(input("Enter the Number: "))
print("="*40)
temp1=num
rev=0
while(num!=0):
    temp = num % 10
    rev = rev * 10 + temp
    num = num // 10
print("{} reversed number is {}".format(temp1,rev))
print("="*40)