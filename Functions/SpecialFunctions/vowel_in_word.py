# to find whether the word contains at least one vowel or not by using filter()
def vow_word(val):
    vowel = list('aeiouAEIOU')
    for ch in val:
        if ch in vowel:
            return True

# main program
lst = []
i = 0
while True:
    var = input("Enter the {}th value(to stop press '!): ".format(i))
    if var == '!':
        break
    if var.isalpha():
        lst.append(var)
    i += 1
print()
word = list(filter(vow_word, lst))
print("vowels list: ", word)
