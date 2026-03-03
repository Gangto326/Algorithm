import sys
from collections import deque

def solve():
    MAX_VALUE = 10_000_000
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))

    for tc in range(T):
        N, M, K = int(next(iterator)), int(next(iterator)), int(next(iterator))
        edge_list = [[] for _ in range(N + 1)]

        for _ in range(K):
            start, end, cost, length = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))
            edge_list[start].append((end, cost, length))

        for i in range(1, N + 1):
            edge_list[i].sort(key=lambda x: (x[0], x[2], x[1]))
            new_edges = []
            current_end = -1
            min_cost = MAX_VALUE

            for end, cost, length in edge_list[i]:
                if end != current_end:
                    current_end = end
                    min_cost = MAX_VALUE

                if cost < min_cost:
                    new_edges.append((end, cost, length))
                    min_cost = cost

            edge_list[i] = new_edges

        DP = [[MAX_VALUE] * (M + 1) for _ in range(N + 1)]
        queue = deque()
        queue.append((0, 0, 1))
        DP[1][0] = 0

        while queue:
            length, cost, node = queue.popleft()

            if DP[node][cost] < length:
                continue

            for next_node in edge_list[node]:
                end, c, l = next_node
                nc = cost + c
                nl = length + l

                if nc <= M:
                    if DP[end][nc] > nl:

                        for i in range(nc, M + 1):
                            if DP[end][i] > nl:
                                DP[end][i] = nl
                            else:
                                break
                        
                        queue.append((nl, nc, end))
        
        answer = min(DP[N])
        if answer == MAX_VALUE:
            print("Poor KCM")
        else:
            print(answer)


if __name__ == "__main__":
    solve()