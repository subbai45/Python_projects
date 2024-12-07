# input the values of in a list
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