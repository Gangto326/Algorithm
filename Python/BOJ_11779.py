import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    board = [[float('inf') for i in range(N+1)] for j in range(N+1)]

    M = int(read().rstrip())
    for _ in range(M):
        start, end, cost = map(int, read().split())
        board[start][end] = min(board[start][end], cost)

    start, end = map(int, read().split())
    dijkstra = []
    start_root = []
    start_root.append(start)
    heapq.heappush(dijkstra, (0, start, start_root))

    check = [[float('inf')] * (N+1) for _ in range(N+1)]
    while dijkstra:
        total, index, root = heapq.heappop(dijkstra)

        if index == end:
            print(total)
            print(len(root))
            print(*root)
            break

        for i in range(1, N+1):
            if board[index][i] != float('inf'):
                if check[index][i] > total+board[index][i]:
                    check[index][i] = total+board[index][i]
                    next_root = root.copy()
                    next_root.append(i)
                    heapq.heappush(dijkstra, (total+board[index][i], i, next_root))


if __name__ == "__main__":
    solve()