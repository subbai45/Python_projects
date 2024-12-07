# to perform the list operation by giving commands as str input

lst=[]
N = int(input("Enter the number to do how many operations: "))
i = type(10)
f = type(10.0)
s = type('s')
b = type(True)
c = type(2+3j)
for _ in range(N):
    cmd = input("Enter the function name along with value: ").split()

    if cmd[0] == 'append':
        lst.append(float(cmd[1]))
    elif cmd[0] == 'insert':
        lst.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == 'index':
        lst.index(int(cmd[1]))
    elif cmd[0] == 'clear':
        lst.clear(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(cmd)<2:
            lst.pop()
        else:
            lst.pop(int(cmd[1]))
    elif cmd[0] == 'sort':
        lst.sort()
    elif cmd[0] == 'reverse':
        lst.reverse()
    elif cmd[0] == 'count':
        lst.count(int(cmd[1]))
    elif cmd[0] == 'print':
        print(lst)
    elif cmd[0] == 'remove':
        lst.remove(int(cmd[1]))
    else:
        print("Please enter valid functions of list")