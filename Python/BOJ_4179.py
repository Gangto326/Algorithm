import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    R, C = map(int, read().split())
    board = [['T'] * (C+2)] + [['T'] + list(read().rstrip()) + ['T'] for _ in range(R)] + [['T'] * (C+2)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    fire_list = []

    start_r, start_c = 0, 0
    for row in range(1, R+1):
        for col in range(1, C+1):
            if board[row][col] == 'J':
                start_r, start_c = row, col
                board[row][col] = '.'
            
            elif board[row][col] == 'F':
                fire_list.append((row, col))
    
    BFS = deque()
    BFS.append((start_r, start_c, 0))

    check = [[True] * (C+2) for _ in range(R+2)]
    check[start_r][start_c] = False
    answer = 0

    while True:
        next_BFS = deque()

        if answer:
            break

        next_fire = []

        for fire in fire_list:
            row, col = fire

            for i in range(4):
                nr, nc = row + dx[i], col + dy[i]

                if board[nr][nc] == '.':
                    board[nr][nc] = 'F'
                    next_fire.append((nr, nc))

        while BFS:
            row, col, time = BFS.popleft()

            if answer:
                break

            time += 1
            for i in range(4):
                nr, nc = row + dx[i], col + dy[i]

                if board[nr][nc] == 'T':
                    answer = time
                    break
                
                if board[nr][nc] == '.' and check[nr][nc]:
                    next_BFS.append((nr, nc, time))
                    check[nr][nc] = False

        if not next_BFS:
            break
        
        fire_list = next_fire
        BFS = next_BFS

    print(answer if answer else "IMPOSSIBLE")


if __name__ == "__main__":
    solve()