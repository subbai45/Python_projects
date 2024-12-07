#to count the each and every charcters in a given line of string, numerics,alphabets,special characters.

sen = input("Enter the line of string: ")
alpha_cnt,num_cnt,sp_cnt,space_cnt= 0,0,0,0
if(len(sen)<=0):
    print("="*50)
    print("Invalid Input,Pleasse enter any str data")
    print("=" * 50)
for ch in sen:
    if(ch.isalpha()):
        alpha_cnt += 1
    elif(ch.isdigit()):
        num_cnt += 1
    elif(ch == " "):
        space_cnt += 1
    else:
        sp_cnt += 1
print("="*50)
print("Total Alphabets in the string data is {}".format(alpha_cnt))
print("-"*50)
print("Total Number of digits in the string data is {}".format(num_cnt))
print("-"*50)
print("Total Special characters in the string data is {}".format(sp_cnt))
print("-"*50)
print("Total spaces in the string data is {}".format(space_cnt))
print("-"*50)
#print("alpha {}, numbers {}, special char {}".format(alpha_cnt,num_cnt,sp_cnt))
print("Total string length is {}".format(len(sen)))
print("="*50)