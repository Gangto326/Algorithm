import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M, K = int(next(iterator)), int(next(iterator)), int(next(iterator))
    node_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, cost = int(next(iterator)), int(next(iterator)), int(next(iterator))
        node_list[a].append((b, cost))
        node_list[b].append((a, cost))
    
    dijkstra = []
    heapq.heappush(dijkstra, (0, 1, K))

    check = [[float('inf')] * (K + 1) for _ in range(N + 1)]
    check[1] = [0] * (K + 1)

    if K >= N - 1:
        print(0)
        return

    while dijkstra:
        total, node, count = heapq.heappop(dijkstra)

        if total > check[count][node]:
            continue

        if node == N:
            print(total)
            return
        
        for next_node, cost in node_list[node]:
            next_total = total + cost

            if check[next_node][count] > next_total:
                check[next_node][count] = next_total
                heapq.heappush(dijkstra, (next_total, next_node, count))
            
            if count and check[next_node][count-1] > total:
                check[next_node][count-1] = total
                heapq.heappush(dijkstra, (total, next_node, count - 1))


if __name__ == "__main__":
    solve()