# display the only alphabets without using function

sen=input("Enter the sentence: ").upper()
cnt=0
print("="*50)
for ch in sen:
    if (ord(ch) in range(65,91) or ord(ch) in range(97,123)or ord(ch)==32):
        print(ch,end='')
        cnt=cnt+1
print()
print("Number of Alphabets are: ",cnt)
print("="*50)