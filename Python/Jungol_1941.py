import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    node_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, read().split())
        node_list[start].append((end, cost))
    
    dijkstra = []
    heapq.heappush(dijkstra, (0, 1))

    check = [float('inf')] * (N + 1)
    check[1] = 0

    while dijkstra:
        total, node = heapq.heappop(dijkstra)

        if node == N:
            print(total)
            return
        
        if check[node] < total:
            continue
        
        for next_node, c in node_list[node]:
            next_cost = total + c

            if check[next_node] > next_cost:
                check[next_node] = next_cost
                heapq.heappush(dijkstra, (next_cost, next_node))


if __name__ == "__main__":
    solve()