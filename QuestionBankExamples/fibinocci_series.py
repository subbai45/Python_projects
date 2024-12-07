# to print the fibonacci series upto the given number
import time
print("="*60)
print("\tFor loop")
print("="*60)
num = int(input("Enter the range of fib series: "))
start = time.time()
n1,n2 = 0,1
print("Fibonacci series: ",n1,n2,end=" ")
for i in range(2,num+1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3,end=" ")
end = time.time()
total_time = end-start
print("\nStart time: ",start)
print("End time: ",end)
print("Total time: ",total_time)
print()
print("---------------------")
print("="*60)
print("\tWhile loop")
print("="*60)
n1,n2 = 0,1
start_t = time.time()
print("Fibonacci series: ",n1,n2,end=" ")
while True:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3 <= num:
        print(n3,end=" ")
    else:
        break
end_t = time.time()
total = end_t-start_t
print("\nStart time: ",start_t)
print("End time: ",end_t)
print("Total time: ",total)

print("="*60)
print("\tRecursive method")
print("="*60)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

#Main program
start_time = time.time()
if num <= 0:
    print("invalid input")
else:
    print("Fibonacci series: ")
    for i in range(num+1):
        print(fib(i),end=" ")
end_time = time.time()
total_t = end_time - start_time
print("\nStart time: ",start_time)
print("End time: ",end_time)
print("Total time: ",total_t)