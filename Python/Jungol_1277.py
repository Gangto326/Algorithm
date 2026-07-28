import sys
from collections import deque

def solve():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    read = sys.stdin.readline
    N = int(read())
    board = [['#'] * (N + 2)] + [['#'] + list(read().strip()) + ['#'] for _ in range(N)] + [['#'] * (N + 2)]

    sr, sc = 0, 0

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if board[row][col] == 'S':
                sr, sc = row, col
                break

    BFS = deque()
    check = [[None] * (N + 2) for _ in range(N + 2)]

    BFS.append((sr, sc))
    check[sr][sc] = (sr, sc)
    
    er, ec = 0, 0
    while BFS:
        r, c = BFS.popleft()

        if board[r][c] == 'E':
            er, ec = r, c
            break
        
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]

            if board[nr][nc] == '#':
                continue

            if check[nr][nc] == None:
                check[nr][nc] = (r, c)
                BFS.append((nr, nc))

    short_list = []
    ir, ic = check[er][ec]

    while True:
        if check[ir][ic] == (ir, ic):
            break

        short_list.append((ir, ic))
        ir, ic = check[ir][ic]
    
    for xr, xc in short_list:
        BFS.clear()
        check = [[None] * (N + 2) for _ in range(N + 2)]

        BFS.append((sr, sc))
        check[sr][sc] = (sr, sc)

        board[xr][xc] = '#'
        flag = False

        while BFS:
            r, c = BFS.popleft()

            if board[r][c] == 'E':
                flag = True
                break
            
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]

                if board[nr][nc] == '#':
                    continue

                if check[nr][nc] == None:
                    check[nr][nc] = (r, c)
                    BFS.append((nr, nc))

        if not flag:
            board[xr][xc] = 'o'
        else:
            board[xr][xc] = '.'

    answer = ""
    for row in range(1, N + 1):
        answer += "".join(board[row][1:-1]) + "\n"
    
    print(answer.rstrip())


if __name__ == "__main__":
    solve()