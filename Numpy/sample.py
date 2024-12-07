# to find the odd number from the 3-d array by using filter function

import numpy as np
import math
import functools as ft

start = int(input("Enter the low value of randint function: "))
end = int(input("Enter the high value of randint function: "))

arr = np.random.randint(start,end,(3,3,3))
print(f"Dimension-{arr.ndim},size-{arr.size},shape-{arr.shape},type-{arr.dtype},\n {arr}")

odd_num = lambda val: val %2 != 0
even_num = lambda val: val %2 == 0

mul_num = lambda val: val % 5 == 0
# Main Program
'''odd_list = []
even_list = []'''
flat_arr = arr.flatten()
odd_list = list(map(int,filter(odd_num,flat_arr)))
even_list = list(map(int,filter(even_num,flat_arr)))
mul_list = list(map(int,filter(mul_num,flat_arr)))

print("\nEven list: ",even_list)
print("-"*60)
print("Odd list: ",odd_list)
print("-"*60)
print("Mul list: ",mul_list)

'''print()
print(len(even_list),len(odd_list))
len_even_ = len(even_list)
len_odd_ = len(odd_list)
factors_even_list = list(filter(lambda i: len_even_ % i == 0,range(1,len_even_+1)))
factors_odd_list = list(filter(lambda i: len_odd_ % i == 0,range(1,len_odd_+1)))

print("sort-even{} and sort-odd{}".format(sorted(even_list),sorted(odd_list)))
print(type(factors_odd_list),type(factors_even_list))

even_list=np.array(even_list)
odd_list=np.array(odd_list)
print(even_list,odd_list)'''

