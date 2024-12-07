# to display the sum of first 'n' natural numbers by using loops

num=int(input("Enter the number: "))
sum=0
if (num<=0):
    print("=" * 50)
    print("Invalid Number,please enter only positive Number")
else:
    for i in range(1,num+1):
        sum=sum+i
    else:
        print("=" * 50)
        print("The sum of natural numbers from 1 to {} is {}".format(num, sum))
        print("=" * 50)
print("-"*50)
print("\t\t\tanother logic")
print("-"*50)
i=1
if(num<=0):
    print("Invalid input, Please enter positive number")
    print("=" * 50)
else:
    sum=0
    while(i<=num):
        sum=sum+i
        i=i+1
    else:
        print("=" * 50)
        print("The sum of natural numbers from 1 to {} is {}".format(num, sum))
        print("=" * 50)
