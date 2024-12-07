# to display only the special characters by using continue statement
print("="*64)
sen=input("Enter the sentence: ")
print("="*64)
cnt=0
if(len(sen)<=0):
    print("Invalid Input, Enter atleast any word")
for ch in sen:
    if((ord(ch) in range(65,91)) or (ord(ch) in range(97,123)) or (ord(ch) in range(48,58))):
        continue
    else:
        print(ch,end=",")
        cnt += 1
print()
print("-"*64)
print("Total number of special characters in the given sentence is ",cnt)
print("="*64)
