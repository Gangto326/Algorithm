import sys
from collections import deque

read = sys.stdin.readline
N = int(read().rstrip())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board = [[0] * 501 for _ in range(501)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, read().split())

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            board[i][j] = 1

M = int(read().rstrip())

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            board[i][j] = 2

BFS = deque()
BFS.append((0, 0, 0))

check = [[False] * 501 for _ in range(501)]
answer = -1
while BFS:
    x, y, cost = BFS.popleft()

    for way in range(4):
        nx, ny = x+dx[way], y+dy[way]

        if nx < 0 or ny < 0 or nx > 500 or ny > 500:
            continue

        if board[nx][ny] == 2 or check[nx][ny]:
            continue

        check[nx][ny] = True
        
        if board[nx][ny] == 0:
            BFS.appendleft((nx, ny, cost))
        else:
            BFS.append((nx, ny, cost+1))

    if x == 500 and y == 500:
        answer = cost
        break
print(answer)