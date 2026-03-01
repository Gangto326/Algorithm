import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T, K = int(next(iterator)), int(next(iterator))
    DP = [0] * (T + 1)
    DP[0] = 1

    for _ in range(K):
        p, n = int(next(iterator)), int(next(iterator))

        for i in range(T, -1, -1):
            if DP[i]:
                for j in range(1, n + 1):
                    if i + (p * j) <= T:
                        DP[i + (p * j)] += DP[i]
                    else:
                        break
    
    print(DP[-1])


if __name__ == "__main__":
    solve()