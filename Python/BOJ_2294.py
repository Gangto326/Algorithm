import sys

def solve():
    MAX_NUM = 1_000_000

    read = sys.stdin.readline
    N, K = map(int, read().split())
    cost_list = set()
    DP = [MAX_NUM] * (K+1)
    for _ in range(N):
        cost = int(read().rstrip())
        if cost <= K:
            cost_list.add(cost)
            DP[cost] = 1

    for i in range(1, K+1):
        if DP[i] != MAX_NUM:
            for cost in cost_list:
                if i + cost <= K:
                   DP[i+cost] = min(DP[i+cost], DP[i]+1)

    print(DP[-1] if DP[-1] != MAX_NUM else -1)


if __name__ == "__main__":
    solve()