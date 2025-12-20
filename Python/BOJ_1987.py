import sys
from collections import deque

read = sys.stdin.readline
R, C = map(int, read().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board = [[False] * (C+2)] + [[False] + list(read().rstrip()) + [False] for _ in range(R)] + [[False] * (C+2)]
duplicate_set = set()

BFS = deque()
BFS.append((1, 1, 1, 1 << ord(board[1][1])-65))
duplicate_set.add((1, 1, 1 << ord(board[1][1])-65))

answer = 0
while BFS:
    x, y, count, check = BFS.popleft()
    answer = max(answer , count)

    for way in range(4):
        nx, ny = x+dx[way], y+dy[way]

        if board[ny][nx]:
            bit = 1 << ord(board[ny][nx])-65

            if check & bit == 0:
                next_bit = check | bit

                if (nx, ny, next_bit) not in duplicate_set:
                    BFS.append((nx, ny, count+1, next_bit))
                    duplicate_set.add((nx, ny, next_bit))

print(answer)