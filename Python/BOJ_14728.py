import sys

def solve():
    read = sys.stdin.readline
    N, T = map(int, read().split())
    DP = [0] * (T + 1)

    for _ in range(N):
        K, S = map(int, read().split())

        for i in range(T, K - 1, -1):
            DP[i] = max(DP[i], DP[i - K] + S)
    
    print(DP[-1])


if __name__ == "__main__":
    solve()