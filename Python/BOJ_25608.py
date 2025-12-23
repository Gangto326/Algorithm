import sys

read = sys.stdin.readline
N, M = map(int, read().split())

# 왼쪽 누적합 최대, 오른쪽 누적합 최대, 전체 누적합
memo = [[0, 0, 0] for _ in range(N)]

answer = 0
for i in range(N):
    num_list = list(map(int, read().split()))

    center_max = 0
    center_sum = 0
    for j in range(M):
        center_sum += num_list[j]
        center_max = max(center_max, center_sum)

        if center_sum < 0:
            center_sum = 0

    answer = max(answer, center_max)
    memo[i][0] = max(0, num_list[0])

    for j in range(M-1):
        num_list[j+1] += num_list[j]
        if memo[i][0] < num_list[j+1]:
            memo[i][0] = num_list[j+1]
    
    memo[i][2] = num_list[-1]

    memo[i][1] = max(0, num_list[-1])
    for j in range(M-1, 0, -1):
        if memo[i][1] < num_list[-1] - num_list[j-1]:
            memo[i][1] = num_list[-1] - num_list[j-1]

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        max_num = 0
        if memo[i][1] > 0:
            max_num += memo[i][1]
        if memo[j][0] > 0:
            max_num += memo[j][0]

        for k in range(N):
            if k == i or k == j:
                continue

            if memo[k][2] > 0:
                max_num += memo[k][2]
        answer = max(answer, max_num)
        
print(answer)