import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    L, N, B = map(int, read().split())

    edge_list = [[] for _ in range(L + 1)]
    for _ in range(N):
        Xi, Wi, Fi, Ci = map(int, read().split())
        edge_list[Xi].append((Wi, Fi, Ci))

    DP = [[-1] * (B + 1) for _ in range(L + 1)]
    DP[0][0] = 0

    for i in range(L + 1):
        for j in range(B + 1):
            if DP[i][j] != -1:

                for w, fun, cost in edge_list[i]:
                    if (i + w <= L) and (j + cost <= B):
                        DP[i + w][j + cost] = max(DP[i + w][j + cost], DP[i][j] + fun)
    
    answer = -1
    for i in DP[-1]:
        answer = max(answer, i)

    print(answer)
    

if __name__ == "__main__" :
    solve()