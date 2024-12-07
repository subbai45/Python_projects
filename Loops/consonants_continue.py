#to display the consonants from the string by using continue statement
print("="*50)
sen = input("Enter the Sentence: ")
print("="*50)
cnt=0
if(len(sen)<=0):
    print("Invalid Input, Enter any word or sentence")
for ch in sen:
    if(ch in (list("aeiou") or list("AEIOU"))):
        continue
    else:
        print(ch,end=" ")
        cnt += 1
print()
print("-"*50)
print("total number of consonants in the string is ",cnt)
print("="*50)