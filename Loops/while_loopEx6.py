#to display the odd numbers within 'n'

n=int(input("enter the number: "))
while (n >= 1):
    if(n%2!=0):
        print(n,end=" ")
    n=n-1
