import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, K = int(next(iterator)), int(next(iterator))
    DP = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    for _ in range(K):
        start, end = int(next(iterator)), int(next(iterator))
        DP[start][end] = 1
        DP[end][start] = -1
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    continue
                
                if DP[i][k] == 1 and DP[k][j] == 1:
                    DP[i][j] = 1
                    DP[j][i] = -1

    query_num = int(next(iterator))
    for _ in range(query_num):
        start, end = int(next(iterator)), int(next(iterator))

        if DP[start][end] == float('inf'):
            print(0)
        elif DP[start][end] >= 0:
            print(-1)
        else:
            print(1)


if __name__ == "__main__":
    solve()