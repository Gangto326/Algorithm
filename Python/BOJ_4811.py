import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    DP = [[0] * 31 for _ in range(31)]

    for i in range(31):
        DP[0][i] = 1

    for i in range(1, 31):
        for j in range(30):
            if j + 1 <= 30:
                DP[i][j] += DP[i - 1][j + 1]
            
            if j > 0:
                DP[i][j] += DP[i][j - 1]

    while True:
        N = int(next(iterator))

        if not N:
            break

        print(DP[N][0])


if __name__ == "__main__":
    solve()