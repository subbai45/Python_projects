#to display the odd numbers within 'n'

n=int(input("enter the number: "))
i=1
if(n<=0):
    print("Please enter positive integers only")
else:
    while (i <= n):
        print(i,end=" ")
        i += 2

'''
 while(i<=n):
    if(i%2!=0):
        print(i,end=',')
    i=i+1
'''
