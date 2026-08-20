import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    DP = [[False] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        small, big = map(int, read().split())
        DP[small][big] = True

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if not DP[i][k]:
                continue

            for j in range(1, N + 1):
                if DP[k][j]:
                    DP[i][j] = True
    
    answer = 0
    for i in range(1, N + 1):
        count = 0

        for j in range(1, N + 1):
            count += DP[i][j] or DP[j][i]

        if count == N - 1:
            answer += 1
    
    print(answer)


if __name__ == "__main__":
    solve()