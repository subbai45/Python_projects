import re
import pickle
with open (r'E:\Python_fullstack\PYTHON\pycharm_projects\Regular Expressions\student.data','r') as fp:
    sentence = fp.read()
pattern_words = r'[A-Za-z]+'
pattern_numbers = r'[0-9]+'
pattern_uppercase = r'[A-Z][a-z]+'
list_words = re.findall(pattern_words,sentence)
list_numbers = re.findall(pattern_numbers,sentence)
list_uppercase = re.findall(pattern_uppercase,sentence)
print("List of Words: ",list_words)
print("List of Numbers: ",list_numbers)
print("List of Uppercase strings: ",list_uppercase)