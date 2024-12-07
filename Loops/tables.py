print("="*50)
n = int(input('enter the num:'))
if(n<=1):
    print("-"*50)
    print("Invalid input,Enter valid input")
    print("="*50)
for i in range(2,n+1):
    for j in range(1,11):
        #print(i,'*',j,'=',i*j)
	    print("{} x {} = {}".format(i,j,i*j))
    print()
    print("="*50)


#n=int(input('enter the table: '))
#for i in range(1,11):
#    print("{} x {} = {}".format(n,i,n*i))