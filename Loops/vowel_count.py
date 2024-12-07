#to display the vowels and count in a line of string

sen=input("Enter the sentence: ")#.lower() #or .upper()
cnt=0
#vowels= ['a','e','i','o','u','A','E','I','O','U']
print("="*50)
for ch in sen:
    if(ch in  ['a','e','i','o','u','A','E','I','O','U']): #in place of list we can diclare vowels object as we declared already before
        print("vowels in line are: {}".format(ch))
        cnt=cnt+1
print()
print("Number of vowel count is: ",cnt)
print("="*50)