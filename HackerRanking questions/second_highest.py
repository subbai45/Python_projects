# to find the second highest of the list

"""lst=[24,3,4,5,6,7,8,45]
max_lst=max(lst)
sec_max=0
for val in lst:
    print(val)
    if val<max_lst and val>sec_max:
        sec_max=val
print(sec_max)"""

n = int(input())
arr = list(map(int, input().split()))
'''arr_max=max(arr)
sec_max=min(arr)'''
arr_max=arr[0]
sec_max=arr[0]
for val in arr:
    if val > arr_max:
        arr_max = val;
    if val < sec_max:
        sec_max=val
if 2 <= n <= 10 and -100 <= arr_max <= 100:
    for val in arr:
        if arr_max > val and sec_max < val:
            sec_max = val
    print(sec_max)