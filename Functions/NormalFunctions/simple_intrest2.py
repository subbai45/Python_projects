# to calculate the simple intrest by using the functions
#approach 2
def simple_intrest(p,t,r):
    sim_int = (p * t * r) / 100
    tot_amt = p * sim_int
    print("=" * 60)
    print("Simple Intrest of (Principal{},Time{},Rate{}) is {}".format(p, t, r, sim_int))
    print('-' * 60)
    print("Total amount is ", round(tot_amt, 2))
    print("=" * 60)

print("="*60)
p=float(input("Enter the principal: "))
print("-" * 60)
t=float(input("Enter the Time: "))
print("-" * 60)
r=float(input("Enter the Rate of intrest: "))
simple_intrest(p,t,r)
