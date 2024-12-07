import re
while True:
    password = input("Enter the password: ")
    pw_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#!]).{8,}$'
    valid_pw = re.match(pw_pattern,password)
    if valid_pw != None:
        print(f"{password} is valid, Proceed")
        break
    else:
        print(f"{password} is Invalid password,-- Try Again!")