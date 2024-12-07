#To convert the temperature from Fh to C or C to Fh #or Fh to K or K to C or C to K
#formula to convert Celcius to Fahrenheit is '(9/5)*c+32' and Celcius to Kelvin is 'c+273.15'
celcius=float(input("Enter the Celcius: "))
fahrenheit=(9/5)*celcius+32
kelvin=celcius+273.15
print("="*40)
print("Celcius to farenheit is {}".format(fahrenheit))
print("Celcius to Kelvin is {}".format(kelvin))
print("="*40)