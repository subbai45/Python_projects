import re
import pickle
import time

starting_time = time.time()
filename = input("Enter the filename: ")
with open(filename,'rb') as fp:
    sentence = pickle.load(fp)
    print(f"{filename} File loaded successfully")
phone_pattern = r'[789]\d{9}'
all_phone_pattern = r'\d{10}'
mail_pattern = r'[\w]+@[\w]+.com'
name_pattern = r'[A-Z][a-z]+'
specific_word_pattern = rf'\b{input("Enter any specific word to find: ")}\b'

phone_list = re.findall(phone_pattern,sentence)
all_phone_list = re.findall(all_phone_pattern,sentence)
mail_list = re.findall(mail_pattern,sentence)
name_list = re.findall(name_pattern,sentence)
specific_word_list = re.findall(specific_word_pattern,sentence)

print(f"Phone numbers list(starting '7 8 9'): {phone_list}")
print(f"All phone numbers list: {all_phone_list}")
print(f'All mails ending with .com: {mail_list}')
print(f"All names in the file: {name_list}")
print(f'Specific word mentioned above: {specific_word_list}')

ending_time = time.time()

print(f"Total time taken to process entire ting is: {ending_time-starting_time}")