import re
import pickle
import time
starting_time = time.time()
with open('filename.data','rb') as fp:
    sentence = pickle.load(fp)
pattern = r'[\w]+@[\w]+.com'
name_pattern = r'[A-Z][a-z]+'
list_names = re.findall(name_pattern,sentence)
is_list = re.findall(pattern,sentence)
print(sentence)
print(list_names)
print(is_list)
ending_time = time.time()
print("total time: ",ending_time-starting_time)

