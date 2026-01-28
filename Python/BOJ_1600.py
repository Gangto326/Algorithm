import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    K = int(read().rstrip())
    W, H = map(int, read().split())
    board = [list(map(int, read().split())) for _ in range(H)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    hx = [-1, -1, 1, 1, -2, -2, 2, 2]
    hy = [2, -2, 2, -2, 1, -1, 1, -1]

    check = [[[float('inf')] * (K+1) for _ in range(W)] for _ in range(H)]
    BFS = deque()
    BFS.append((0, 0, 0, K))
    check[0][0][K] = 0

    answer = -1
    while BFS:
        row, col, count, jump_count = BFS.popleft()

        if row == H-1 and col == W-1:
            answer = count
            break
        
        count += 1
        for way in range(4):
            nr, nc = row+dx[way], col+dy[way]

            if nr < 0 or nc < 0 or nr >= H or nc >= W:
                continue
            
            if board[nr][nc] == 1:
                continue

            if check[nr][nc][jump_count] <= count:
                continue
            
            check[nr][nc][jump_count] = count
            BFS.append((nr, nc, count, jump_count))

        jump_count -= 1
        if jump_count < 0:
            continue

        for way in range(8):
            nr, nc = row+hx[way], col+hy[way]

            if nr < 0 or nc < 0 or nr >= H or nc >= W:
                continue

            if board[nr][nc] == 1:
                continue

            if check[nr][nc][jump_count] <= count:
                continue
            
            check[nr][nc][jump_count] = count
            BFS.append((nr, nc, count, jump_count))

    print(answer)


if __name__ == "__main__":
    solve()