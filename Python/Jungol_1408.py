import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = [tuple(map(int, read().split())) for _ in range(N)]
    num_list.sort(key = lambda x: x[0])

    DP = [1] * N
    for i in range(N - 1, -1, -1):
        for j in range(i, N):
            if num_list[i][1] < num_list[j][1]:
                DP[i] = max(DP[i], DP[j] + 1)
    
    print(N - max(DP))


if __name__ == "__main__":
    solve()