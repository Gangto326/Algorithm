import sys

read = sys.stdin.readline
N, M = map(int, read().split())
num_list = [0] + list(map(int, read().split()))
sorted_dict = {value : index for index, value in enumerate(sorted(num_list))}

num_list = [sorted_dict[i] for i in num_list]

node_list = [[] for _ in range(N+1)]
check_list = [False] * (N+1)

for _ in range(M):
    u, v = map(int, read().split())

    if num_list[u] > num_list[v]:
        node_list[u].append(v)
    else:
        node_list[v].append(u)

K = int(read().rstrip())
k_list = list(map(int, read().split()))
for i in k_list:
    check_list[i] = True

answer = "no flood"
for i in range(1, N+1):
    if not check_list[i]:
        for j in node_list[i]:
            if check_list[j]:
                check_list[i] = True
                break
    
    if not check_list[i]:
        answer = "flood"
        break

print(answer)