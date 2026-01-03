import sys

read = sys.stdin.readline
R, C = map(int, read().split())

input_list = [read().rstrip() for _ in range(R)]
str_list = []

for i in range(C):
    next_str = ""

    for str in input_list:
        next_str += str[i]
    
    str_list.append(next_str)


left = 0
right = R
while left < right:
    mid = (left + right) // 2

    check = set()
    for str in str_list:
        check.add(str[mid:])
    
    if len(check) == C:
        left = mid + 1
    else:
        right = mid

print(left-1)