# Replace all occurrences of a specific word in a text with another word.
# Replace all consecutive spaces in a string with a single space.

import re
with open(r'E:\Python_fullstack\PYTHON\pycharm_projects\Regular Expressions\student.data','r') as fp:
    sentence = fp.read()
    print(sentence)
sub_word = 'mail'

replaced_sentence = re.sub(rf'\b{sub_word}\b','Gmail',sentence)

print(replaced_sentence)