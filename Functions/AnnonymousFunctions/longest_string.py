# Find the Longest String:
# Use a lambda function to find the longest string in a list.
import functools
dic = {}
lst = input("Enter the list of words: ").split()
str_len = lambda x,y: x if len(x)>len(y) else y
each_str_len = lambda x:len(x)
each_len = list(map(each_str_len,lst))
len_str = functools.reduce(str_len,lst)
for val in lst:
    dic[val]=len(val)
print(dic)
print(len_str)