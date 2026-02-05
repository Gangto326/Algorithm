import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M, K = map(int, read().split())
    board = [[1] * (N+2)] + [[1] + list(map(int, read().split())) + [1] for _ in range(N)] + [[1] * (N+2)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_row, start_col = map(int, read().split())
    end_dict = {}
    for i in range(2, M+2):
        r, c, er, ec = map(int, read().split())

        board[r][c] = i
        end_dict[i] = (er, ec)
    
    
    for _ in range(M):
        BFS = deque()
        BFS.append((start_row, start_col, 0))

        mr, mc, min_count, person = 0, 0, float('inf'), 0
        check = [[True] * (N+2) for _ in range(N+2)]
        check[start_row][start_col] = False

        while BFS:
            row, col, count = BFS.popleft()

            if min_count < count:
                break

            if board[row][col] >= 2:
                
                if min_count == count:
                    if row > mr:
                        continue
                    
                    if row == mr and col > mc:
                        continue
                    
                    mr, mc, min_count, person = row, col, count, board[row][col]
                
                else:
                    mr, mc, min_count, person = row, col, count, board[row][col]
            
            for i in range(4):
                nr, nc = row + dx[i], col + dy[i]

                if board[nr][nc] == 1:
                    continue

                if not check[nr][nc]:
                    continue
                
                check[nr][nc] = False
                BFS.append((nr, nc, count + 1))
        
        K -= min_count
        if K <= 0:
            K = -1
            break
        
        BFS = deque()
        BFS.append((mr, mc, 0))
        er, ec = end_dict[person]
        check = [[True] * (N+2) for _ in range(N+2)]
        check[mr][mc] = False
        board[mr][mc] = 0

        min_count = -1
        while BFS:
            row, col, count = BFS.popleft()

            if row == er and col == ec:
                min_count = count
                break
            
            for i in range(4):
                nr, nc = row + dx[i], col + dy[i]

                if board[nr][nc] == 1:
                    continue

                if not check[nr][nc]:
                    continue
                
                check[nr][nc] = False
                BFS.append((nr, nc, count + 1))

        if min_count == -1:
            K = -1
            break
        
        K -= min_count

        if K < 0:
            K = -1
            break
        
        K += (min_count * 2)
        start_row, start_col = er, ec

    print(K)


if __name__ == "__main__":
    solve()