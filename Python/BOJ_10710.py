import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]
    weather_list = [int(next(iterator)) for _ in range(M)]

    DP = [[float('inf')] * (N + 1) for _ in range(M + 1)]
    for i in range(M + 1):
        DP[i][0] = 0

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            DP[i][j] = min(DP[i - 1][j], DP[i - 1][j - 1] + weather_list[i - 1] * num_list[j - 1])
    
    print(DP[-1][-1])


if __name__ == "__main__":
    solve()