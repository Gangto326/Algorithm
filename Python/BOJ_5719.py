import sys, heapq
from collections import deque

def solve():
    read = sys.stdin.readline

    while True:
        N, M = map(int, read().split())

        if N == 0 and M == 0:
            break

        start, end = map(int, read().split())
        board = [[float('inf')] * (N) for _ in range(N)]
        
        for _ in range(M):
            S, D, cost = map(int, read().split())
            board[S][D] = min(board[S][D], cost)
        
        parents = [[] for _ in range(N)]
        check = [float('inf')] * (N)
        check[start] = 0
        dijkstra = []
        heapq.heappush(dijkstra, (0, start))

        min_length = float('inf')
        while dijkstra:
            total, node = heapq.heappop(dijkstra)

            if total > min_length:
                break

            if node != start and check[node] < total:
                continue

            if node == end:
                min_length = total

            else:
                for i in range(N):
                    if board[node][i] == float('inf'):
                        continue
                    
                    next_total = total + board[node][i]
                    if check[i] > next_total:
                        check[i] = next_total
                        parents[i] = [node]
                        heapq.heappush(dijkstra, (next_total, i))
                    
                    elif check[i] == next_total:
                        parents[i].append(node)


        BFS = deque()
        BFS.append(end)
        visited = [False] * N
        visited[end] = True

        while BFS:
            node = BFS.popleft()

            for parent in parents[node]:
                board[parent][node] = float('inf')

                if not visited[parent]:
                    BFS.append(parent)
                    visited[parent] = True


        check = [float('inf')] * (N)
        dijkstra = []
        heapq.heappush(dijkstra, (0, start))

        answer = float('inf')
        while dijkstra:
            total, node = heapq.heappop(dijkstra)

            if node == end:
                answer = total
                break

            for i in range(N):
                if board[node][i] == float('inf'):
                    continue
                
                next_total = total + board[node][i]
                if check[i] > next_total:
                    check[i] = next_total
                    heapq.heappush(dijkstra, (next_total, i))

        print(answer if answer != float('inf') else -1)
        

if __name__ == "__main__":
    solve()