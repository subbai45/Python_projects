#to display the sum of digits of giveen number

num=int(input("Enter the Number: "))
sum=0
temp=num
print("="*50)
if(num<=0):
    print("Invalid Input,Please Enter positive integers only")
    print("="*50)
while(num!=0):
    rem=num%10
    num=num//10
    sum=sum+rem
else:
    print("Sum of Digits of given number {} is {}".format(temp,sum))
    print("="*50)

