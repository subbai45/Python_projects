# to check whether the name if valid or not
while(1):
    print("="*50)
    name=input("Enter the Name: ")
    print("=" * 50)
    val_name=name.split()
    res=True
    for val in val_name:
        if(not val.isalpha()):
            res=False
            break
    if(res==True):
        print("'{}' is Valid Name".format(name))
        print("=" * 50)
        break
    else:
        print("'{}' is Invalid Name,Please Enter Again".format(name))
        print("=" * 50)
