# to print the list of words,whose word length is ranges from the given range by using filter()
def word_len(word):
    if len(word) in range(word_start_range,word_end_range+1):
        return True
    else:
        return False

# Main Program
lst=[]
i=0
while True:
    val= input("Enter the {}th value(To Stop press '!'): ".format(i))
    if(val =='!'):
        break
    lst.append(val)
    i += 1
word_start_range = int(input("Enter tha range of the word: "))
word_end_range = int(input("Enter tha range of the word: "))
print()
word = list(filter(word_len,lst))
print()
print("list of word whose range is between {} to {} are {}".format(word_start_range,word_end_range,word))