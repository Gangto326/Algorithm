import sys

def solve():
    read = sys.stdin.readline
    T = int(read())
    K = int(read())
    DP = [0] * (T + 1)
    DP[0] = 1

    for _ in range(K):
        cost, count = map(int, read().split())

        for i in range(T, -1, -1):
            if DP[i]:
                for c in range(1, count + 1):
                    if i + cost * c <= T:
                        DP[i + cost * c] += DP[i]
    
    print(DP[-1])


if __name__ == "__main__":
    solve()