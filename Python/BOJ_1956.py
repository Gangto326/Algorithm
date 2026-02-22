import sys

def solve():
    MAX_VALUE = 10_000_000
    read = sys.stdin.readline
    V, E = map(int, read().split())
    DP = [[MAX_VALUE] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        start, end, cost = map(int, read().split())
        DP[start][end] = min(DP[start][end], cost)


    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
    

    answer = MAX_VALUE
    for i in range(1, V + 1):
        answer = min(answer, DP[i][i])
    
    print(answer if answer != MAX_VALUE else -1)


if __name__ == "__main__":
    solve()