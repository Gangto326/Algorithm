import sys, heapq

def solve():
    read = sys.stdin.buffer.readline
    N, M = map(int, read().split())
    node_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, cost = map(int, read().split())
        node_list[a].append((b, cost))
        node_list[b].append((a, cost))
    
    X, Z = map(int, read().split())
    P = int(read())
    point_list = [X] + list(map(int, read().split())) + [Z]
    point_count = len(point_list)
    board = [[float('inf')] * point_count for _ in range(point_count)]

    for i in range(point_count - 1):
        start = point_list[i]
        dist = [float('inf')] * (N + 1)

        dijkstra = []
        dist[start] = 0
        heapq.heappush(dijkstra, (0, start))

        while dijkstra:
            cost, node = heapq.heappop(dijkstra)

            if dist[node] < cost:
                continue

            for next_node, c in node_list[node]:
                next_cost = cost + c

                if dist[next_node] > next_cost:
                    dist[next_node] = next_cost
                    heapq.heappush(dijkstra, (next_cost, next_node))
        
        for index in range(point_count):
            board[i][index] = dist[point_list[index]]
    
    ALL_VISITED = 1 << (point_count - 1)
    DP = [[float('inf')] * ALL_VISITED for _ in range(point_count - 1)]
    DP[0][1] = 0

    for visited in range(1, ALL_VISITED):
        if not visited & 1:
            continue

        for i in range(point_count - 1):
            if not visited & (1 << i):
                continue

            prev_visited = visited ^ (1 << i)

            for j in range(point_count - 1):
                if i == j:
                    continue

                if not prev_visited & (1 << j):
                    continue

                if DP[j][prev_visited] == float('inf'):
                    continue

                DP[i][visited] = min(DP[i][visited], DP[j][prev_visited] + board[j][i])
    
    answer = float('inf')
    for i in range(point_count - 1):
        answer = min(answer, DP[i][ALL_VISITED - 1] + board[i][point_count - 1])
    
    print(answer if answer != float('inf') else -1)


if __name__ == "__main__":
    solve()