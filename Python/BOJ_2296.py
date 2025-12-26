import sys

read = sys.stdin.readline
N = int(read())
spots = sorted([tuple(map(int, read().split())) for _ in range(N)], key = lambda x: x[0])

up_DP = [0] * N
down_DP = [0] * N
for i in range(N):
    cost = spots[i][2]
    up_DP[i] = cost
    down_DP[i] = cost

    for j in range(i):

        if spots[j][1] > spots[i][1]:
            down_DP[i] = max(down_DP[i], down_DP[j] + cost)
        
        else:
            up_DP[i] = max(up_DP[i], up_DP[j] + cost)
    
print(max(max(up_DP), max(down_DP)))