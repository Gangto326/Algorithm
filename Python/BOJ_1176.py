import sys

read = sys.stdin.read().split()
iterator = iter(read)

N, K = int(next(iterator)), int(next(iterator))
height_list = [int(next(iterator)) for _ in range(N)]
DP = [[0] * N for _ in range(1 << N)]

for i in range(N):
    DP[1 << i][i] += 1

for check in range(1 << N):
    for i in range(N):
        if DP[check][i] == 0:
            continue

        for j in range(N):
            bit_j = 1 << j

            if check & bit_j == 0 and abs(height_list[i] - height_list[j]) > K:
                DP[check | bit_j][j] = DP[check][i] + DP[check | bit_j][j]

answer = sum(DP[(1 << N) - 1])
print(answer)