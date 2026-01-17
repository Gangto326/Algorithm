import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    node_list = [[] for _ in range(N+1)]

    for _ in range(N-1):
        start, end = map(int, read().split())
        node_list[start].append(end)
        node_list[end].append(start)

    DP = [[float('inf')] * (N+1) for _ in range(2)]


    def DFS(index, parent):
        nonlocal node_list, DP

        next_nodes = node_list[index]
        DP[0][index] = 0
        DP[1][index] = 1
        
        for next_node in next_nodes:
            if next_node != parent:
                DFS(next_node, index)
                DP[0][index] += DP[1][next_node]
                DP[1][index] += min(DP[0][next_node], DP[1][next_node])
    

    DFS(1, -1)
    print(min(DP[0][1], DP[1][1]))


if __name__ == "__main__":
    solve()