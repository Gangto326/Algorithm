import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        L, R, C = map(int, read().split())

        if L == R == C == 0:
            break
        
        board_list = []
        start_r, start_c, start_h = 0, 0, 0
        end_r, end_c, end_h = 0, 0, 0

        for h in range(L):
            board = [list(read().rstrip()) for _ in range(R)]

            for row in range(R):
                for col in range(C):
                    if board[row][col] == 'S':
                        start_r, start_c, start_h = row, col, h
                        board[row][col] = '.'
                    elif board[row][col] == 'E':
                        end_r, end_c, end_h = row, col, h
                        board[row][col] = '.'

            read()
            board_list.append(board)
        
        BFS = deque()
        BFS.append((start_r, start_c, start_h, 0))

        check = [[[True] * C for _ in range(R)] for _ in range(L)]
        check[start_h][start_r][start_c] = False

        answer = 0
        while BFS:
            row, col, h, count = BFS.popleft()

            if row == end_r and col == end_c and h == end_h:
                answer = count
                break
            
            count += 1
            for i in range(4):
                nr, nc = row + dx[i], col + dy[i]

                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue

                if board_list[h][nr][nc] == '#':
                    continue

                if not check[h][nr][nc]:
                    continue

                BFS.append((nr, nc, h, count))
                check[h][nr][nc] = False

            if h > 0:
                if board_list[h-1][row][col] == '.' and check[h-1][row][col]:
                    BFS.append((row, col, h-1, count))
                    check[h-1][row][col] = False

            if h < L-1:
                if board_list[h+1][row][col] == '.' and check[h+1][row][col]:
                    BFS.append((row, col, h+1, count))
                    check[h+1][row][col] = False

        if not answer:
            print("Trapped!")
        else:
            print(f"Escaped in {answer} minute(s).")
            

if __name__ == "__main__":
    solve()