import sys, heapq
sys.setrecursionlimit(1050)

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    edge_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        first, sec, cost = map(int, read().split())
        edge_list[first].append((sec, cost))
        edge_list[sec].append((first, cost))

    dijkstra = []
    heapq.heappush(dijkstra, (0, 1))
    
    check = [float('inf')] * (N + 1)
    check[1] = 0

    route = [[] for _ in range(N + 1)]
    while dijkstra:
        cost, node = heapq.heappop(dijkstra)

        if check[node] < cost:
            continue

        if node == N:
            break

        for next_node, c in edge_list[node]:
            next_cost = cost + c

            if check[next_node] > next_cost:
                check[next_node] = next_cost
                route[next_node] = [node]
                heapq.heappush(dijkstra, (next_cost, next_node))
            
    original_check_N = check[N] 
    
    answer = -1
    def DFS(index):
        nonlocal N, answer, route

        if index == 1 or not route[index]:
            return

        for curr in route[index]:
            DFS(curr)
            dijkstra = []
            heapq.heappush(dijkstra, (0, 1))

            check = [float('inf')] * (N + 1)
            check[1] = 0

            while dijkstra:
                cost, node = heapq.heappop(dijkstra)

                if check[node] < cost:
                    continue

                if node == N:
                    break

                for next_node, c in edge_list[node]:
                    if (node == index and next_node == curr) or (node == curr and next_node == index):
                        continue

                    next_cost = cost + c

                    if check[next_node] > next_cost:
                        check[next_node] = next_cost
                        heapq.heappush(dijkstra, (next_cost, next_node))

            answer = max(answer, check[N])
        

    DFS(N)
    print(answer - original_check_N if answer != float('inf') else -1)


if __name__ == "__main__":
    solve()