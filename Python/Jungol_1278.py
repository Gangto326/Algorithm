import sys

def solve():
    read = sys.stdin.readline
    N, W = map(int, read().split())

    DP = [0] * (W + 1)
    for _ in range(N):
        w, p = map(int, read().split())

        for i in range(W - w, -1, -1):
            DP[i + w] = max(DP[i + w], DP[i] + p)
    
    print(max(DP))


if __name__ == "__main__":
    solve()