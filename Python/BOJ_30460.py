import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = [0] + list(map(int, read().split())) + [0, 0]
    DP = [-float('inf')] * (N + 3)
    DP[0] = 0

    for i in range(1, N + 3):
        DP[i] = max(DP[i], DP[i - 1] + num_list[i])

        if i >= 3:
            DP[i] = max(DP[i], (num_list[i - 2] + num_list[i - 1] + num_list[i]) * 2 + DP[i - 3])

    print(DP[-1])


if __name__ == "__main__" :
    solve()