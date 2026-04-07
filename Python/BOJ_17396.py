import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]
    node_list = [[] for _ in range(N)]

    for _ in range(M):
        a, b, cost = int(next(iterator)), int(next(iterator)), int(next(iterator))
        
        if (not num_list[a] or a == N - 1) and (not num_list[b] or b == N - 1):
            node_list[a].append((b, cost))
            node_list[b].append((a, cost))
    
    dijkstra = []
    heapq.heappush(dijkstra, (0, 0))

    check = [float('inf')] * N
    check[0] = 0

    answer = -1
    while dijkstra:
        cost, node = heapq.heappop(dijkstra)

        if check[node] < cost:
            continue

        if node == N - 1:
            answer = cost
            break
        
        for next_node, c in node_list[node]:
            next_cost = cost + c

            if check[next_node] > next_cost:
                check[next_node] = next_cost
                heapq.heappush(dijkstra, (next_cost, next_node))

    print(answer)
    

if __name__ == "__main__":
    solve()