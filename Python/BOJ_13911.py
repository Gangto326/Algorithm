import sys, heapq

def solve():
    read = sys.stdin.buffer.read().split()
    iterator = iter(read)
    V, E = int(next(iterator)), int(next(iterator))
    node_list = [[] for _ in range(V + 2)]

    for _ in range(E):
        u, v, w = int(next(iterator)), int(next(iterator)), int(next(iterator))
        node_list[u].append((v, w))
        node_list[v].append((u, w))

    M, x = int(next(iterator)), int(next(iterator))
    for _ in range(M):
        node_list[0].append((int(next(iterator)), 0))
    
    S, y = int(next(iterator)), int(next(iterator))
    for _ in range(S):
        node_list[V + 1].append((int(next(iterator)), 0))

    mac_list = [float('inf')] * (V + 2)
    star_list = [float('inf')] * (V + 2)

    
    def dijkstra(index, li, limit):
        heap = []
        heapq.heappush(heap, (0, index))
        li[index] = 0
        
        while heap:
            cost, node = heapq.heappop(heap)

            if li[node] < cost:
                continue

            for next_node, c in node_list[node]:
                next_cost = cost + c

                if next_cost > limit:
                    continue

                if li[next_node] > next_cost:
                    li[next_node] = next_cost
                    heapq.heappush(heap, (next_cost, next_node))


    dijkstra(0, mac_list, x)
    dijkstra(V + 1, star_list, y)

    answer = float('inf')
    for i in range(1, V + 1):
        if mac_list[i] != 0 and star_list[i] != 0:
            answer = min(answer, mac_list[i] + star_list[i])
    
    print(answer if answer != float('inf') else -1)


if __name__ == "__main__":
    solve()