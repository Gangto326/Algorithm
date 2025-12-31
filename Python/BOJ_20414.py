import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())

    s, g, p, d = map(int, read().split())
    mvp_dict = {'B': (0, s-1), 'S': (s, g-1), 'G': (g, p-1), 'P': (p, d-1), 'D': (d, float('inf'))}
    month_list = list(read().rstrip())

    DP = [[-1] * 501 for _ in range(N)]

    min_cost, max_cost = mvp_dict[month_list[0]]
    for i in range(d+1):
        if min_cost <= i <= max_cost:
            DP[0][i] = i

    for i in range(1, N):
        min_cost, max_cost = mvp_dict[month_list[i]]

        for j in range(d+1):
            for k in range(d+1):
                if j+k > max_cost:
                    break

                if DP[i-1][k] == -1:
                    continue

                if min_cost <= j+k:
                    DP[i][j] = max(DP[i][j], DP[i-1][k]+j)

    print(max(DP[-1]))


if __name__ == "__main__":
    solve()