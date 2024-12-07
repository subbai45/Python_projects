# to calculate the simple intrest by using the functions
#approach 1
def simple_intrest():
    print("="*60)
    p=float(input("Enter the principal: "))
    print("-" * 60)
    t=float(input("Enter the Time: "))
    print("-" * 60)
    r=float(input("Enter the Rate of intrest: "))

    sim_int=(p*t*r)/100
    tot_amt=p*sim_int

    return p,t,r,sim_int,tot_amt

res=simple_intrest()
print("="*60)
print("Simple Intrest of (Principal{},Time{},Rate{}) is {}".format(res[0],res[1],res[2],res[3]))
print('-'*60)
print("Total amount is ",round(res[4],2))
print("="*60)