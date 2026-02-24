import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    node_cost = [0] * (N + 1)
    node_list = [[] for _ in range(N + 1)]

    for i in range(N):
        node_cost[i + 1] = int(next(iterator))
    
    for _ in range(M):
        a, b, length = int(next(iterator)), int(next(iterator)), int(next(iterator))
        node_list[a].append((b, length))
        node_list[b].append((a, length))
    
    dijkstra = []
    heapq.heappush(dijkstra, (0, 1, node_cost[1]))

    check = [float('inf')] * (N + 1)
    while dijkstra:
        total, node, cost = heapq.heappop(dijkstra)

        if check[node] <= cost:
            continue

        check[node] = cost

        if node == N:
            print(total)
            return

        for next_node, length in node_list[node]:
            next_total = total + (length * cost)
            heapq.heappush(dijkstra, (next_total, next_node, min(cost, node_cost[next_node])))


if __name__ == "__main__":
    solve()