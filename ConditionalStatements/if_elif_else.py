#using if...elif...else statement display the word of its digit

digit = int(input("enter the digit: "))

print("=" * 27)
if (digit == 0):
    print("\t{} is Zero".format(digit))
elif (digit == 1):
    print("\t{} is One".format(digit))
elif (digit == 2):
    print("\t{} is Two".format(digit))
elif (digit == 3):
    print("\t{} is Three".format(digit))
elif (digit == 4):
    print("\t{} is Four".format(digit))
elif (digit == 5):
    print("\t{} is Five".format(digit))
elif (digit == 6):
    print("\t{} is Six".format(digit))
elif (digit == 7):
    print("\t{} is Seven".format(digit))
elif (digit == 8):
    print("\t{} is Eight".format(digit))
elif (digit == 9):
    print("\t{} is Nine".format(digit))
elif (-9 <= digit < 0):
    print("\t{} is Negative Digit".format(digit))
elif (-9 > digit) or (9 < digit):
    print("\t{} is Number".format(digit))
print("=" * 27)
