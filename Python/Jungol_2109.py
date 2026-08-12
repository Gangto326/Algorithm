import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M, X = map(int, read().split())

    edge_list = [[] for _ in range(N + 1)]
    reversed_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = map(int, read().split())

        edge_list[start].append((end, cost))
        reversed_list[end].append((start, cost))
    

    def find_cost(li):
        nonlocal N, X

        dijkstra = []
        heapq.heappush(dijkstra, (0, X))

        check = [float('inf')] * (N + 1)
        check[X] = 0

        while dijkstra:
            total, node = heapq.heappop(dijkstra)

            if check[node] < total:
                continue

            for next_node, cost in li[node]:
                next_total = total + cost

                if check[next_node] > next_total:
                    check[next_node] = next_total
                    heapq.heappush(dijkstra, (next_total, next_node))
        
        return check
    

    go_X = find_cost(edge_list)
    arrived_X = find_cost(reversed_list)

    answer = 0
    for i in range(1, N + 1):
        answer = max(answer, go_X[i] + arrived_X[i])
    
    print(answer)


if __name__ == "__main__":
    solve()