import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    M, N, H = map(int, read().split())

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    BFS = deque()

    tomato = 0
    board_list = []
    for h in range(H):
        board = [list(map(int, read().split())) for _ in range(N)]
        board_list.append(board)

        for row in range(N):
            for col in range(M):
                if board[row][col] == 1:
                    BFS.append((h, row, col, 0))
                elif board[row][col] == 0:
                    tomato += 1

    if not tomato:
        print(0)
        return
    
    while BFS:
        h, row, col, day = BFS.popleft()
        day += 1

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if board_list[h][nr][nc] == 0:
                board_list[h][nr][nc] = 1
                tomato -= 1
                BFS.append((h, nr, nc, day))
            
        if h > 0 and board_list[h-1][row][col] == 0:
            board_list[h-1][row][col] = 1
            tomato -= 1
            BFS.append((h-1, row, col, day))
        
        if h < H-1 and board_list[h+1][row][col] == 0:
            board_list[h+1][row][col] = 1
            tomato -= 1
            BFS.append((h+1, row, col, day))

        if not tomato:
            print(day)
            return
    
    print(-1)


if __name__ == "__main__":
    solve()