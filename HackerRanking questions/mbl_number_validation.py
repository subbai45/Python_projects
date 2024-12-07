# to validate the mobile umber by using the regular expressions
import re
'''num = int(input("Enter the number of mobile number to want: "))
if 1 <= num <= 10:
    for _ in range(1,num+1):
        number = input()
        print(number)
        qun = re.search(r"[987]\d{9}",number)
        if qun != None:
            print(f"+91 {number}")
            print('yes')
        else:
            print(f"+91 {number}")
            print('no')'''

'''num = int(input())
if 1 <= num <= 10:
    for _ in range(1,num+1):
        number = input()
        if 2 <= len(number) <= 15:
            re_exp = re.match(r"[987]\d {9}$",number)
            if re_exp != None:
                print('YES')
            else:
                print('NO')'''

import re

# Function to validate mobile number
def validate_mobile(number):
    # Check if the input matches exactly a 10-digit number starting with 7, 8, or 9
    if re.fullmatch(r"[789]\d{9}", number):
        return True
    return False

# Get the number of mobile numbers to validate
num = int(input("Enter how many mobile numbers you want to validate: "))

# Ensure the number of entries is within valid range (1 to 10)
if 1 <= num <= 10:
    for _ in range(num):
        number = input("Enter mobile number: ")
        if validate_mobile(number):
            print(f"+91 {number}")
            print('yes')  # Valid mobile number
        else:
            print(f"+91 {number}")
            print('no')  # Invalid mobile number
else:
    print("Please enter a number between 1 and 10.")
