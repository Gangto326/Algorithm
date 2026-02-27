import sys

def solve():
    MAX_VALUE = 10_000_000
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    edge_list = []
    DP = [[MAX_VALUE] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b, length = int(next(iterator)), int(next(iterator)), int(next(iterator))
        DP[a][b] = min(DP[a][b], length)
        DP[b][a] = min(DP[b][a], length)
        edge_list.append((a, b, length))

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            DP[i][i] = 0

            for j in range(1, N + 1):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
    
    answer = float('inf')
    for node in range(1, N + 1):
        max_value = 0

        for edge in edge_list:
            max_value = max(max_value, (DP[node][edge[0]] + DP[node][edge[1]] + edge[2]) / 2)
        
        answer = min(answer, max_value)
    
    answer = int(answer * 10)
    print(answer / 10)


if __name__ == "__main__":
    solve()