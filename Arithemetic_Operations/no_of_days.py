#To convert the given days into years,monts and remaining days

days_in_year=365
days_in_month=30
days=int(input("Enter the days to convert: "))
l_year=days//days_in_year
rem_days=days%days_in_year
l_month=rem_days//days_in_month
l_days=rem_days%days_in_month
print("="*100)
print("Total number of days in terms of years-months-days are : {} years - {} months - {} days".format(l_year,l_month,l_days))
print("="*100)


#To convert the given days into years,monts and remaining days
'''
days_in_year=365
days_in_month=30
days=int(input("Enter the days to convert: "))
l_year=days//days_in_year
temp=days-(days_in_year*l_year)
l_month=temp//days_in_month
temp=temp-(days_in_month*l_month)
l_days=temp
print("="*100)
print("Total number of days in terms of years-months-days are : {} years - {} months - {} days".format(l_year,l_month,l_days))
print("="*100)
'''

