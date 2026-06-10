import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    C, R = map(int, read().split())
    board = [[0] * (C + 2)] + [[0] + list(map(int, list(read().strip()))) + [0] for _ in range(R)] + [[0] * (C + 2)]
    start_col, start_row = map(int, read().split())

    BFS = deque()
    BFS.append((start_row, start_col, 0))
    check = [[True] * (C + 2) for _ in range(R + 2)]
    check[start_row][start_col] = False

    time = 0
    while BFS:
        r, c, count = BFS.popleft()
        time = count

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]

            if board[nr][nc] and check[nr][nc]:
                check[nr][nc] = False
                BFS.append((nr, nc, count + 1))

    print(time + 3)
    live = 0
    for i in range(R + 2):
        for j in range(C + 2):
            if board[i][j] and check[i][j]:
                live += 1
    
    print(live)
    

if __name__ == "__main__":
    solve()