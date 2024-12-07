#to display the multiples of any number
n=int(input("enter the number: "))
i=1
if(n<=0):
    print("please enter positive number only")
else:
    while (i <= 10):
        print("{} x {} = {}".format(n, i, n * i))
        i = i + 1