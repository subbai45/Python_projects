d=int(input("enter the digit: "))


print("="*27)
if(d==0):
    print("\t{} is Zero".format(d))
if(d==1):
    print("\t{} is One".format(d))
if(d==2):
    print("\t{} is Two".format(d))
if(d==3):
    print("\t{} is Three".format(d))
if(d==4):
    print("\t{} is Four".format(d))
if(d==5):
    print("\t{} is Five".format(d))
if(d==6):
    print("\t{} is Six".format(d))
if(d==7):
    print("\t{} is Seven".format(d))
if(d==8):
    print("\t{} is Eight".format(d))
if(d==9):
    print("\t{} is Nine".format(d))
if(-9<=d<0):
    print("\t{} is Negative Digit".format(d))
if(-9>d) or (9<d):
    print("\t{} is Number".format(d))
print("="*27)