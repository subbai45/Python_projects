#check whether in the given word there is atleast one vowel or not

word=input("Enter the Word: ")
res="vowel word" if (('a' in word)or('e' in word)or('i' in word)or('o' in word)or('u' in word)|('A' in word)or('E' in word)or('I' in word)or('O' in word)or('U' in word)) else "not Vowel word"
print("="*(len(word)+(30)))
print("\t{} is {}".format(word,res))
print("="*(len(word)+(30)))