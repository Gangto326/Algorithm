import sys, heapq

def solve():
    read = sys.stdin.readline
    T = int(read())

    for tc in range(T):
        N, D, C = map(int, read().split())

        node_list = [[] for _ in range(N + 1)]
        for _ in range(D):
            end, start, cost = map(int, read().split())
            node_list[start].append((end, cost))
        
        dijkstra = []
        heapq.heappush(dijkstra, (0, C))
        check = [float('inf') for _ in range(N + 1)]
        check[C] = 0

        while dijkstra:
            cost, node = heapq.heappop(dijkstra)

            if check[node] < cost:
                continue

            for next_node, c in node_list[node]:
                next_cost = c + cost
                
                if check[next_node] > next_cost:
                    check[next_node] = next_cost
                    heapq.heappush(dijkstra, (next_cost, next_node))

        answer = 0
        min_cost = 0

        for i in range(1, N + 1):
            if check[i] != float('inf'):
                answer += 1
                min_cost = max(min_cost, check[i])

        print(answer, min_cost)


if __name__ == "__main__":
    solve()