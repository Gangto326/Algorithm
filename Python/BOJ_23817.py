import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board = [['X'] * (M+2)] + [['X'] + list(read().rstrip()) + ['X'] for _ in range(N)] + [['X'] * (M+2)]

restaurants = 1
restaurants_list = []
start_row, start_col = 0, 0
for i in range(N+2):
    for j in range(M+2):
        if board[i][j] == 'K':
            board[i][j] = restaurants
            restaurants += 1
            restaurants_list.append((i, j))
        
        elif board[i][j] == 'S':
            board[i][j] = 0
            start_row, start_col = i, j
            restaurants_list = [(i, j)] + restaurants_list

dist_board = [[float('inf')] * restaurants for _ in range(restaurants)]

for i in range(restaurants):
    row, col = restaurants_list[i]
    dist_board[i][i] = 0

    BFS = deque()
    BFS.append((row, col, 0))

    check = [[True] * (M+2) for _ in range(N+2)]
    check[row][col] = False

    while BFS:
        r, c, count = BFS.popleft()

        for way in range(4):
            nr, nc = r + dy[way], c + dx[way]

            if board[nr][nc] == 'X':
                continue
            
            if check[nr][nc]:
                if board[nr][nc] == '.':
                    check[nr][nc] = False
                    BFS.append((nr, nc, count+1))
            
                else:
                    check[nr][nc] = False
                    dist_board[i][board[nr][nc]] = count+1
                    BFS.append((nr, nc, count+1))

answer = float('inf')


def permutation(per_list, check, count, length):
    global answer, dist_board

    if count == 5:
        answer = min(answer, length)
        return

    for i in range(1, restaurants):
        if check & (1 << i) == 0:
            next_length = length+dist_board[per_list[count]][i]

            if next_length < answer:
                per_list.append(i)
                permutation(per_list, check | (1 << i), count+1, next_length)
                per_list.pop()


permutation([0], 0, 0, 0)
print(answer if answer != float('inf') else -1)