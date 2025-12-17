import sys, copy
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board = [[1] * (M+2)] + [[1] + list(map(int, read().split())) + [1] for _ in range(N)] + [[1] * (M+2)]

zero_point = []
virous_point = []
answer = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i][j] == 0:
            zero_point.append((i, j))

        elif board[i][j] == 2:
            virous_point.append((i, j))

def BFS():
    global answer

    copy_board = copy.deepcopy(board)

    queue = deque()
    queue.extend(virous_point)

    while queue:
        x, y = queue.popleft()

        for way in range(4):
            next_x, next_y = x + dx[way], y + dy[way]

            if copy_board[next_x][next_y] == 0:
                queue.append((next_x, next_y))
                copy_board[next_x][next_y] = 2

    count = 0
    for i in range(1,N+1):
        count += copy_board[i].count(0)

    answer = max(answer, count)


def make_wall(start, cnt):
    if cnt == 3:
        BFS()
        return
    
    for i in range(start, len(zero_point)):
        x, y = zero_point[i]

        if board[x][y] == 0:
            board[x][y] = 1
            make_wall(i+1, cnt+1)
            board[x][y] = 0

make_wall(0, 0)
print(answer)