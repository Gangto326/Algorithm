import sys

def solve():
    read = sys.stdin.readline
    N, A = read().split()
    M, B = read().split()

    N, M = int(N), int(M)

    DP = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        DP[i][0] = i
    for j in range(M + 1):
        DP[0][j] = j

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                DP[i][j] = DP[i-1][j-1]
            
            else:
                DP[i][j] = min(DP[i][j-1], DP[i-1][j], DP[i-1][j-1]) + 1

    print(DP[-1][-1])


if __name__ == "__main__":
    solve()