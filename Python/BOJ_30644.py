import sys

read = sys.stdin.readline
N = int(read())

num_list = list(map(int, read().split()))
sorted_list = sorted(num_list)

idx_dict = {val: idx for idx, val in enumerate(sorted_list)}
idx_list = [idx_dict[i] for i in num_list]

answer = 0
index = 0
flag = 0
while index < N-1:
    if idx_list[index] == idx_list[index+1]-1:
        flag = 1
    
    elif idx_list[index] == idx_list[index+1]+1:
        flag = 2
    
    else:
        answer += 1
        index += 1
        flag = 0
        continue

    if flag == 1:
        while index < N-1 and idx_list[index] == idx_list[index+1]-1:
            index += 1
    else:
        while index < N-1 and idx_list[index] == idx_list[index+1]+1:
            index += 1

print(answer)