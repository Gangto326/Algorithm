import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    T = int(read())

    for tc in range(T):
        W, H = map(int, read().split())
        board = [['$'] * (W + 2)] + [['$'] + list(read().strip()) + ['$'] for _ in range(H)] + [['$'] * (W + 2)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        fire_list = []
        sr, sc = 0, 0

        for row in range(1, H + 1):
            for col in range(1, W + 1):
                if board[row][col] == '*':
                    fire_list.append((row, col))
                elif board[row][col] == '@':
                    sr, sc = row, col
                    board[sr][sc] = '.'
        
        BFS = []
        BFS.append((sr, sc))

        check = [[True] * (W + 2) for _ in range(H + 2)]
        check[sr][sc] = False

        answer = 0
        while BFS:
            next_fire = []

            for fr, fc in fire_list:
                for i in range(4):
                    nr, nc = fr + dx[i], fc + dy[i]

                    if board[nr][nc] == '.':
                        board[nr][nc] = '*'
                        next_fire.append((nr, nc))

            next_BFS = []
            flag = False
            for row, col in BFS:
                for i in range(4):
                    nr, nc = row + dx[i], col + dy[i]

                    if board[nr][nc] == '.' and check[nr][nc]:
                        check[nr][nc] = False
                        next_BFS.append((nr, nc))

                    elif board[nr][nc] == '$':
                        flag = True
                        break
            if flag:
                answer += 1
                break

            if next_BFS:
                answer += 1
            else:
                answer = 0
                break

            fire_list = next_fire
            BFS = next_BFS
    
        print(answer if answer != 0 else "IMPOSSIBLE")


if __name__ == "__main__":
    solve()