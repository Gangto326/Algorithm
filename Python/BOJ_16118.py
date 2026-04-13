import sys, heapq

def solve():
    read = sys.stdin.buffer.readline
    N, M = map(int, read().split())
    node_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, cost = map(int, read().split())
        node_list[a].append((b, cost))
        node_list[b].append((a, cost))

    dijkstra = []
    heapq.heappush(dijkstra, (0, 1))

    fox = [float('inf')] * (N + 1)
    fox[1] = 0

    while dijkstra:
        cost, node = heapq.heappop(dijkstra)

        if fox[node] < cost:
            continue

        for next_node, c in node_list[node]:
            next_cost = cost + c

            if fox[next_node] > next_cost:
                fox[next_node] = next_cost
                heapq.heappush(dijkstra, (next_cost, next_node))
    
    dijkstra = []
    heapq.heappush(dijkstra, (0, 1, 0))

    wolf = [[float('inf'), float('inf')] for _ in range(N + 1)]
    wolf[1][0] = 0

    while dijkstra:
        cost, node, fast = heapq.heappop(dijkstra)

        if wolf[node][fast] < cost:
            continue
        
        fast = (fast + 1) % 2
        for next_node, c in node_list[node]:
            next_cost = cost

            if fast:
                next_cost += (c / 2)
            else:
                next_cost += (c * 2)

            if wolf[next_node][fast] > next_cost:
                wolf[next_node][fast] = next_cost
                heapq.heappush(dijkstra, (next_cost, next_node, fast))

    answer = 0
    for i in range(1, N + 1):
        if fox[i] < min(wolf[i]):
            answer += 1
    
    print(answer)


if __name__ == "__main__":
    solve()