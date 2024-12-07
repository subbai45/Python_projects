#To Calculate the Simple Interest and Total Amount to pay
#Formula to caculate the simple interest is - (PTR)/100 and Total Amount to pay is - P+SI

P=float(input("Enter the Principal amount: "))
R=float(input("Enter the Rate of Interest: "))
T=float(input("Enter the Time periiod: "))
SI=(P*T*R)/100
TotAmt=P+SI
print("="*50)
print("Simple Interest is {}".format(SI))
print("Total Amount to Pay is {}".format(TotAmt))
print("="*50)