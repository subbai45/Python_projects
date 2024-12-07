# to print the months of calendar of the specific year
import calendar as c
years=[] #empty list of years
while(1):
    lst=input("Enter the years(to stop press '!': ")
    print("-"*40)
    if(lst=='!'): #to stop the loop
        break
    years.append(int(lst)) #to add the given inputs in the list
print()
for mon in years: #list of years
    print("="*20)
    for i in range(1,13): #range of months from 1 to 13-1 (12)
        print("-"*20)
        print(c.month(mon,i)) #(mon is year and i is month)
        print("-"*20)
        print("\n")
    print("=" * 20)