import sys

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())

    items = {}
    for _ in range(N):
        A, B = map(int, input().split())
        if B in items:
            items[B] = min(items[B], A)
        else:
            items[B] = A

    DP = [[-1] * (K+1) for _ in range(5001)]
    DP[1][1] = 1

    answer = 1
    for i in range(1, K):
        for j in range(1, 5001):
            if DP[j][i] == -1:
                continue

            DP[j][i+1] = max(DP[j][i+1], DP[j][i]+j)
            answer = max(answer, DP[j][i+1])

            for B, A in items.items():
                if DP[j][i] >= A:
                    DP[j+B][i+1] = max(DP[j+B][i+1], DP[j][i]-A)
                    answer = max(answer, DP[j+B][i+1])

    print(answer)


if __name__ == "__main__":
    solve()