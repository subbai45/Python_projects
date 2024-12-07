import re

with open(r'E:\Python_fullstack\PYTHON\pycharm_projects\Regular Expressions\student.data','r') as fp:
    sentence = fp.read()
email_pattern = r'\w+@[a-z.]+\.[a-z]{2,}'
list_mails = re.findall(email_pattern,sentence)
print(sentence)
print("List of Mails: ",list_mails)