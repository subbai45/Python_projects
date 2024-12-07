# Filter the even number and store them in list by using special functions (filter,map,reduce) with help of anonymous function

# Intermediate level
import functools as ft

lst = list(map(float,input().split()))
lst1 = [(1, 3), (4, 1), (2, 2), (5, 0),(4,9),(7,8)]
words = input("Enter the string to find whether word is palindrome or not: ").split()
even_res = {}

# anonymous functions
even_or_not = lambda val: True if val % 2 == 0 else False
even_num1 = lambda val:val if val %2 ==0 else None
even_num = lambda val: val % 2 == 0
square_num = lambda val: val**2
sorted_list = lambda val: sorted(val[1])
sum_list = lambda a,b: a+b
pal_list = lambda word: word == word[::-1]

# main program
for val in lst:
    res = even_or_not(val)
    if res == True:
        res = 'Even'
    else:
        res = 'Odd'
    even_res[val] = res

even_res1 = list((filter(even_or_not, lst)))
res_filter = list(filter(even_num, lst))
res_map = list(map(even_num1,lst))
square_res = list(map(square_num,lst))
sorted_res = sorted(lst1,key=lambda val:val[1])
sum_res = ft.reduce(sum_list,lst)

pal_res = list(filter(pal_list,words))

print(even_res)
print(even_res1)
print(res_filter)
print(square_res)
print(res_map)
print(sorted_res)
print(sum_res)
print("palindrome list: ", pal_res)
