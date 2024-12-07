# Input Format x,y,z and n Four integers  and , each on a separate line.
# Print the list in lexicographic increasing order.

print("Enter the values")
x=int(input("x value: "))
y=int(input("y value: "))
z=int(input("z value: "))
n=int(input("enter the n value: "))#where x+y+z should not increase the n;

print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+z) != n))

print("------------------------or--------------------------")

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != n:
               print( list([i,j,k]),end="," )