#n = int(input())
integer_list = map(int, input().split())
tpl = tuple(integer_list)
print(hash(tpl))
