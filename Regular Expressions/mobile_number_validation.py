import re

while True:
    try:
        number = input('Enter the mobile number: ')
        mbl_pattern = r'[789]\d{9}'
        valid_number = re.search(mbl_pattern,str(number))
        if valid_number != None:
            print(f"{number} is Valid Number")
            break
        else:
            print(f"{number} is Invalid Mobile Number -- Try again!")
    except (ValueError or TypeError):
        print(f"Invalid Input, Check the number while entering input")