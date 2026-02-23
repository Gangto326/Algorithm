import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))

    DP = [0] * 10010
    DP[0] = 1
    for i in range(1, 4):
        for j in range(10001):
            if DP[j]:
                DP[j + i] += DP[j]

    for tc in range(T):
        N = int(next(iterator))
        print(DP[N])


if __name__ == "__main__":
    solve()