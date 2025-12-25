import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    H, W = map(int, read().split())
    board = [list(read().rstrip()) for _ in range(H)]

    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]

    BFS = deque()
    for row in range(H):
        for col in range(W):
            if board[row][col] != '.' and board[row][col] != '9':
                BFS.append((row, col, 0))

    answer = 0
    while BFS:
        dump = deque()
        check = set()
        change_list = []

        flag = False
        while BFS:
            row, col, count = BFS.popleft()

            if board[row][col] == '.':
                continue

            empty_count = 0
            for way in range(8):
                nr, nc = row+dy[way], col+dx[way]
                empty_count += board[nr][nc] == '.'

            if empty_count >= int(board[row][col]):
                flag = True
                change_list.append((row, col))

                for way in range(8):
                    nr, nc = row+dy[way], col+dx[way]

                    if board[nr][nc] != '.' and board[nr][nc] != '9':
                        if not (nr, nc) in check:
                            dump.append((nr, nc, count+1))
                            check.add((nr, nc))
        
        BFS = dump
        check = set()
        if flag:
            answer += 1

        for row, col in change_list:
            board[row][col] = '.'

    print(answer)

if __name__ == '__main__':
    solve()