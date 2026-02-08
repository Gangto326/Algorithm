import sys

def solve():
    MOD = 1_000_000_000
    read = sys.stdin.readline
    N, K = map(int, read().split())
    DP = [[1] * (N+1)] + [[0] * (N+1) for _ in range(K-1)]

    for time in range(1, K):
        for num in range(N+1):
            for i in range(N+1-num):
                DP[time][num+i] += DP[time-1][i] % MOD
                DP[time][num+i] %= MOD
    
    print(DP[-1][-1])


if __name__ == "__main__":
    solve()