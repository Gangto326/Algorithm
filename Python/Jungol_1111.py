import sys, heapq

def solve():
    read = sys.stdin.readline
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    N = int(read())
    end_r, end_c = map(int, read().split())
    board = [[0] * (N + 2)] + [[0] + list(map(int, read().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]

    dijkstra = []
    heapq.heappush(dijkstra, (0, end_r, end_c))

    check = [[float('inf')] * (N + 2) for _ in range(N + 2)]
    check[end_r][end_c] = 0

    while dijkstra:
        cost, r, c = heapq.heappop(dijkstra)

        if check[r][c] < cost:
            continue

        if board[r][c] == 0:
            print(cost)
            return
        
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]

            if board[r][c] > board[nr][nc]:
                next_cost = cost + ((board[r][c] - board[nr][nc]) ** 2)

                if check[nr][nc] > next_cost:
                    check[nr][nc] = next_cost
                    heapq.heappush(dijkstra, (next_cost, nr, nc))
            
            elif board[r][c] < board[nr][nc]:
                next_cost = cost + abs(board[r][c] - board[nr][nc])

                if check[nr][nc] > next_cost:
                    check[nr][nc] = next_cost
                    heapq.heappush(dijkstra, (next_cost, nr, nc))
            
            else:
                if check[nr][nc] > cost:
                    check[nr][nc] = cost
                    heapq.heappush(dijkstra, (cost, nr, nc))


if __name__ == "__main__":
    solve()