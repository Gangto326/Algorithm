import sys

def solve():
    MOD = 1_000_000_003
    N, K = map(int, sys.stdin.read().split())
    DP = [[0] * (K + 1) for _ in range(N + 1)]

    if K * 2 > N:
        print(0)
        return

    for i in range(N + 1):
        DP[i][0] = 1
        DP[i][1] = i

    for i in range(2, N + 1):
        for j in range(2, K + 1):
            DP[i][j] = (DP[i-1][j] + DP[i-2][j-1]) % MOD
    
    answer = (DP[N-3][K-1] + DP[N-1][K]) % MOD
    print(answer)


if __name__ == "__main__":
    solve()