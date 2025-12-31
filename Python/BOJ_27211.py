import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())

board = [list(read().split()) for _ in range(N)]
check = [[True] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            start_list.append((i, j))

BFS = deque()

answer = 0
for sx, sy in start_list:
    if check[sx][sy]:
        answer += 1

        BFS.append((sx, sy))
        check[sx][sy] = False

        while BFS:
            x, y = BFS.popleft()

            for way in range(4):
                nx, ny = x+dx[way], y+dy[way]

                if nx < 0:
                    nx += N
                elif ny < 0:
                    ny += M
                
                nx, ny = nx % N, ny % M

                if board[nx][ny] == '0' and check[nx][ny]:
                    BFS.append((nx, ny))
                    check[nx][ny] = False
                
print(answer)