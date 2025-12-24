import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    DP = [0] + [-float("inf")] * (M+1)
    curse_list = [[0, 0]] + [list(map(int, read().split())) for _ in range(M)] + [[N+1, 0]]
    curse_sum = [Y for X, Y in curse_list]

    for i in range(1, M+1):
        curse_sum[i] += curse_sum[i-1]

    for i in range(1, M+2):
        for j in range(i):
            days = curse_list[i][0] - curse_list[j][0] - 1
            total_curse = curse_sum[i-1] - curse_sum[j]
            DP[i] = max(DP[i], DP[j] + (days * (days+1)) / 2 - total_curse)

    print(int(DP[-1]))

if __name__ == "__main__":
    solve()