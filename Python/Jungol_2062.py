import sys

def solve():
    N = int(sys.stdin.readline())

    DP = [[0] * (N + 1) for _ in range(5)]
    DP[0][0] = 1

    for i in range(1, int(N ** 0.5) + 1):
        num = i ** 2

        for j in range(1, 5):
            for k in range(num, N + 1):
                DP[j][k] += DP[j - 1][k - num]
    
    print(sum(DP[i][-1] for i in range(1, 5)))


if __name__ == "__main__":
    solve()