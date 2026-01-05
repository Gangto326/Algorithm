import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    N, M, K = map(int, read().split())

    candy_list = [0] + list(map(int, read().split()))
    parents = [i for i in range(N+1)]


    def find(index):
        nonlocal parents

        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]


    def union(first, sec):
        nonlocal parents

        fp = find(first)
        sp = find(sec)

        if fp != sp:
            parents[fp] = sp


    for _ in range(M):
        first, sec = map(int, read().split())
        union(first, sec)

    for i in range(1, N+1):
        find(i)

    DP = [-1] * (K)
    DP[0] = 0
    tree_dict = {}

    for i in range(1, N+1):
        if parents[i] in tree_dict:
            tree_dict[parents[i]][0] += candy_list[i]
            tree_dict[parents[i]][1] += 1
        else:
            tree_dict[parents[i]] = [candy_list[i], 1]

    for key, value in tree_dict.items():
        for i in range(K-1, -1, -1):
            if DP[i] != -1 and i + value[1] < K:
                DP[i+value[1]] = max(DP[i+value[1]], DP[i] + value[0])

    print(max(DP))


if __name__ == "__main__":
    solve()