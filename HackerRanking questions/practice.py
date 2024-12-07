i = type(10)
f = type(10.0)
s = type('s')
b = type(True)
c = type(2+3j)
print(i,f,s,b,c)
lst=[1,24.5,'subbai',True,2+3j]

if type(lst[1]) == i:
    print('int')
if type(lst[1]) == f:
    print('float')
if type(lst[2]) == s:
    print('str')