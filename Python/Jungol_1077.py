import sys

def solve():
    read = sys.stdin.readline
    N, W = map(int, read().split())
    jewels = [tuple(map(int, read().split())) for _ in range(N)]
    DP = [0] * (W + 1)

    for w, p in jewels:
        for i in range(W + 1):
            if i + w > W:
                break

            DP[i + w] = max(DP[i + w], DP[i] + p)
    
    print(DP[-1])


if __name__ == "__main__":
    solve()