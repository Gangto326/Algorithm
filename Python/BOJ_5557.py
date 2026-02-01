import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    DP = [[0] * 21 for _ in range(N-1)]
    DP[0][num_list[0]] = 1

    for i in range(1, N-1):
        num = num_list[i]

        for j in range(21):
            if DP[i-1][j] and j + num <= 20:
                DP[i][j+num] += DP[i-1][j]

            if DP[i-1][j] and j - num >= 0:
                DP[i][j-num] += DP[i-1][j]

    print(DP[-1][num_list[-1]])


if __name__ == "__main__":
    solve()