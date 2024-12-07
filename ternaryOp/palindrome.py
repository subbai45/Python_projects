#check whether word is palindrome or not

word=input("Enter the word: ")
res="Palindrome" if word==word[::-1] else "Not Palindrome"
# if input is 12421 then giving output as palindrome,'bug code'.
print("="*40)
print("\t{} is {}".format(word,res))
print("="*40)