#print the only alphabets in a given line of string
print("="*50)
sen=input("Enter the sentence: ")#.lower()
print("="*50)
for ch in sen:
    if(ch.isalpha()):
        print(ch,end="")
print()
print("-"*50)
i=0
while(i<len(sen)):
    if(sen[i].isalpha()):
        print(sen[i],end="")
    i+=1
print()
print("="*50)