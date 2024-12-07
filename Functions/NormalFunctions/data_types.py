# To find the data type of given object and display its type
def data_type(obj):
    if(type(obj)==int):
        print("{} is Integer object".format(obj))
    elif(type(obj)==float):
        print("{} is Float object".format(obj))
    elif (bool(obj) == bool):
        print("{} is Bool object".format(obj))
    elif (type(obj) == complex):
        print("{} is complex object".format(obj))
    elif (type(obj) == str):
        print("{} is str object".format(obj))
    elif (type(obj) == range):
        print("{} is range object".format(obj))
    elif (type(obj) == bytes):
        print("{} is bytes object".format(obj))
    elif (type(obj) == bytearray):
        print("{} is bytearray object".format(obj))
    elif (type(obj) == list):
        print("{} is list object".format(obj))
    elif (type(obj) == tuple):
        print("{} is tuple object".format(obj))
    elif (type(obj) == set):
        print("{} is set object".format(obj))
    elif (type(obj) == frozenset):
        print("{} is frozenset object".format(obj))
    elif (type(obj) == dict):
        print("{} is dict object".format(obj))
    else:
        print("{} is NoneType object".format(obj))

var=10,20,30,40
b=bytes(var)
data_type(var)