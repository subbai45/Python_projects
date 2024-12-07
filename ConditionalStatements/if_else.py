#using if...else statement display the word of its digit

digit=float(input("Enter the Digit: "))
print("="*20)
if(digit==0):
    print("{} is Zero".format(digit))
else:
    if(digit==1):
        print("{} is One".format(digit))
    else:
        if(digit == 2):
            print("{} is Two".format(digit))
        else:
            if(digit==3):
                print("{} is Three".format(digit))
            else:
                if(digit==4):
                    print("{} is Four".format(digit))
                else:
                    if(digit==5):
                        print("{} is Five".format(digit))
                    else:
                        if(digit==6):
                            print("{} is Six".format(digit))
                        else:
                            if(digit==7):
                                print("{} is Seven".format(digit))
                            else:
                                if(digit==8):
                                    print("{} is Eight".format(digit))
                                else:
                                    if(digit==9):
                                        print("{} is Nine".format(digit))
                                    else:
                                        if(-9<=digit<0):
                                            print("{} is -Ve Digit".format(digit))
                                        else:
                                            if(-9>digit or digit>9):
                                                print("{} is Number".format(digit))

print("="*20)
print("Program execution completed")


