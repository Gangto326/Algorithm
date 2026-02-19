import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    DP = [0] * (N+2)

    for i in range(1, N+1):
        T, P = int(next(iterator)), int(next(iterator))
        DP[i] = max(DP[i], DP[i-1])

        if i + T > N + 1:
            continue

        DP[i + T] = max(DP[i + T], DP[i] + P)

    print(max(DP[-1], DP[-2]))


if __name__ == "__main__":
    solve()