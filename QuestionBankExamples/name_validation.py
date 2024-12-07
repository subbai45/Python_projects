# 3. Write a Python Program for Validating Name of a Person OR Product Name or Place Name:
# Sample Input: Guido Van Rossum----Valid Name bcoz all alphabets are present
# Sample Input: Gui$do Van Rossum----InValid Name bcoz $ symbols not allowed
# Sample Input: Gui2do Van R-ossum----InValid Name bcoz 2 (digit) and  special symbol(-) are not allowed

while True:
    name = input("Enter the Name: ").title()
    sp_cnt = 0
    sp_wd = []
    res = True
    for i in name:
        if not(i.isalpha() or i.isspace()):
            res = False
            if i.isdigit():
                sp_cnt += 1
            else:
                sp_wd.append(i)
    if res:
        print(f"{name} is Valid Name because all alphabets are present")
        break

    else:
        if sp_cnt > 0 and sp_wd:
            print(f"{name} Invalid Name because it contains {sp_cnt} digits and {''.join(sp_wd)} symbols are not allowed")
        elif sp_cnt:
            print(f"{name} Invalid Name because it contains {sp_cnt} digits")
        elif len(sp_wd) == 1:
            print(f"{name} is Invalid Name because {''.join(sp_wd)} symbols not allowed")
        print("Please Enter Name Again")