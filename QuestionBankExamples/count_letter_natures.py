# 1) Write a Python Program to Count Uppercase and Lowercase and special symbols (except spaces) in a  given Line text.
# Sample Input: NaResh I TeCh


def sample_input():
    sam_inp = input("Enter the Sample Input: ")
    upper ,lower,sp = 0,0,0
    for i in sam_inp:
        if ord('A') <= ord(i) <= ord('Z'):
            upper += 1
        elif ord('a') <= ord(i) <= ord('z'):
            lower += 1
        else:
            sp += 1
    return upper,lower,sp
# Main Program

count = sample_input()
print("Count of upper case letters are ",count[0])
print("Count of Lower case letters are ",count[1])
print("Count of special character letters are ",count[2])