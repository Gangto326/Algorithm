import sys, heapq

def solve():
    read = sys.stdin.readline
    W, H = map(int, read().split())
    board = [['*'] * (W + 2)] + [['*'] + list(read().strip()) + ['*'] for _ in range(H)] + [['*'] * (W + 2)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    sr, sc = 0, 0
    er, ec = 0, 0

    for row in range(1, H + 1):
        for col in range(1, W + 1):
            if board[row][col] == 'C':
                board[row][col] = '.'

                if sr == sc == 0:
                    sr, sc = row, col
                else:
                    er, ec = row, col

    check = [[[float('inf')] * 4 for _ in range(W + 2)] for _ in range(H + 2)]

    dijkstra = []
    for i in range(4):
        check[sr][sc][i] = 0
        heapq.heappush(dijkstra, (0, sr, sc, i))
            
    
    while dijkstra:
        cost, row, col, way = heapq.heappop(dijkstra)

        if check[row][col][way] < cost:
            continue
            
        if row == er and col == ec:
            print(cost)
            return
        
        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if board[nr][nc] == '.':
                if i == way:
                    if check[nr][nc][i] > cost:
                        check[nr][nc][i] = cost
                        heapq.heappush(dijkstra, (cost, nr, nc, i))
                
                else:
                    next_cost = cost + 1

                    if check[nr][nc][i] > next_cost:
                        check[nr][nc][i] = next_cost
                        heapq.heappush(dijkstra, (next_cost, nr, nc, i))


if __name__ == "__main__":
    solve()