import sys

read = sys.stdin.readline
N = int(read())
bangboo_list = list(map(int, read().split()))
sorted_list = sorted(bangboo_list)
idx_dict = {val: idx for idx, val in enumerate(sorted_list)}
reversed_idx_dict = {val: abs(idx - (N-1)) for idx, val in enumerate(sorted_list)}

check = [False if idx_dict[bangboo_list[i]] != i else True for i in range(N)]
reversed_check = [False if reversed_idx_dict[bangboo_list[i]] != i else True for i in range(N)]

count = 0
reversed_count = 0

for i in range(N):
    if not check[i]:
        cycle = 0
        curr_idx = i

        while not check[curr_idx]:
            check[curr_idx] = True
            cycle += 1
            curr_idx = idx_dict[bangboo_list[curr_idx]]
    
        count += cycle-1

for i in range(N):
    if not reversed_check[i]:
        cycle = 0
        curr_idx = i

        while not reversed_check[curr_idx]:
            reversed_check[curr_idx] = True
            cycle += 1
            curr_idx = reversed_idx_dict[bangboo_list[curr_idx]]
    
        reversed_count += cycle-1

print(N-2, min(count, reversed_count))