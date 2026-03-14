import sys

def solve():
    read = sys.stdin.readline
    N, X = map(int, read().split())
    DP = [0] * (X + 1)
    DP[0] = 1

    for _ in range(N):
        cost, count = map(int, read().split())

        for i in range(X - cost, -1, -1):
            if DP[i]:
                for j in range(1, count + 1):
                    if i + (cost * j) <= X:
                        DP[i + (cost * j)] += DP[i]
    
    print(DP[-1])


if __name__ == "__main__":
    solve()