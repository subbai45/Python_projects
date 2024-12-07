# Remove all special characters from a string, leaving only letters and numbers.
# Replace all consecutive spaces in a string with a single space.
import re

with open(r'E:\Python_fullstack\PYTHON\pycharm_projects\Regular Expressions\student.data','r') as fp:
    sentence = fp.read()
remove_pattern = r'[^A-Za-z0-9\s]'
space_pattern = r'\s+'
removed_sentence = re.sub(remove_pattern,"",sentence)
space_sentence = re.findall(space_pattern,sentence)
print(f"Space is: {"".join(space_sentence)} to here")
print(removed_sentence)