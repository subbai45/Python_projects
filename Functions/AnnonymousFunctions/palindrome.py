# to find the given word is palindrome or not

pal=lambda word:"palindrome" if word==word[::-1] else "Not Palindrome"

# Main Program
print("="*70)
word=input("Enter the word to test the word is palindrome or not: ").upper()
res=pal(word)

print("="*70)
print("\t\t\t\t'{}' is {}".format(word,res))
print("="*70)