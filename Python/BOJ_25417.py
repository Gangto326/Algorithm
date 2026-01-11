import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    board = [[-1] * 7] + [[-1] + list(map(int, read().split())) + [-1] for _ in range(5)] + [[-1] * 7]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    start_row, start_col = map(int, read().split())
    start_row += 1
    start_col += 1

    check = [[float('inf')] * 7 for _ in range(7)]
    BFS = deque()
    BFS.append((start_row, start_col, 0))
    check[start_row][start_col] = 0

    answer = -1
    while BFS:
        row, col, count = BFS.popleft()

        if board[row][col] == 1:
            answer = count
            break

        for way in range(4):
            nr, nc = row + dx[way], col + dy[way]
            next_count = count + 1

            if board[nr][nc] != -1 and check[nr][nc] > next_count:
                check[nr][nc] = next_count
                BFS.append((nr, nc, next_count))

            while True:
                if board[nr][nc] == -1:
                    nr -= dx[way]
                    nc -= dy[way]
                    break

                if board[nr][nc] == 7:
                    break
                
                nr += dx[way]
                nc += dy[way]
            
            if check[nr][nc] > next_count:
                check[nr][nc] = next_count
                BFS.append((nr, nc, next_count))

    print(answer)


if __name__ == "__main__" :
    solve()