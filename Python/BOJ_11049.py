import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    matrix = [tuple(map(int, read().split())) for _ in range(N)]

    DP = [[0] * N for _ in range(N)]

    for sequence in range(1, N):
        for i in range(N-sequence):
            j = i + sequence
            DP[i][j] = float('inf')

            for k in range(i, j):
                cost = DP[i][k] + DP[k+1][j] + (matrix[i][0] * matrix[k][1] * matrix[j][1])
                DP[i][j] = min(DP[i][j], cost)

    print(DP[0][-1])


if __name__ == "__main__":
    solve()