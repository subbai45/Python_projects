# to write something in the file dynamically

# input the values of in a list
filename=input("Enter the new file name: ")
def input_list():
    lst=[]
    i=0
    while True:
        val = input("Enter the {}th value(To stop press '!'):".format(i)).capitalize()
        if val == '!':
            break
        if(val.isdigit()):
            lst.append(float(val))
        elif (val.isalpha()):
            lst.append(val)
        elif val.isalnum():
            lst.append(val)
        else:
            lst.append(val)
        i += 1
    return lst

list_1=input_list()
with open(filename,'w') as fp:
    list_of_values=fp.write(str(list_1))
