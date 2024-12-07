# 10. Write a Python program to find the list of words that are longer than n from a given list of
# words

def word_len(len_of_words):
    lst = []
    print("choose to print the list of values for LONGER or SMALLER words to print")
    print("""       ====================================
                    Menu to Print words
             ====================================
                1. Longer words
                2. Smaller words
                3. Exact length of words
             ====================================""")
    ch = int(input("choose the option from menu: "))
    match(ch):
        case 1:
            word_length = int(input("Enter the word length: "))
            for val in len_of_words:
                if len(val) >= word_length:
                    lst.append(val)
            return lst
        case 2:
            word_length = int(input("Enter the word length: "))
            for val in len_of_words:
                if len(val) <= word_length:
                    lst.append(val)
            return lst
        case 3:
            word_length = int(input("Enter the word length: "))
            for val in len_of_words:
                if len(val) == word_length:
                    lst.append(val)
            return lst
        case _:
            print("Choose correct option in the given Menu")

#main program
list_of_words=[]
i=0
while True:
    val=input("Enter the {}th values(Press ! to stop): ".format(i))
    if(val == '!'):
        break
    list_of_words.append(val)
    i += 1
print()
final_list=word_len(list_of_words)
print("="*80)
print("Normal list is: ",list_of_words)
print("~"*80)
print("Filtered list is: ",final_list)
print("="*80)