import sys

read = sys.stdin.readline
N, M = map(int, read().split())

board = [[-1] * (M+2)] + [[-1] + list(map(int, read().split())) + [-1] for _ in range(N)] + [[-1] * (M+2)]
tetro_list = [[(0, 0), (1, 0), (2, 0), (3, 0)], 
              [(0, 0), (0, 1), (0, 2), (0, 3)], 
              [(0, 0), (0, 1), (1, 0), (1, 1)], 
              [(0, 0), (0, 1), (0, 2), (1, 2)], 
              [(0, 0), (1, 0), (2, 0), (2, -1)],
              [(0, 0), (1, 0), (1, 1), (1, 2)],
              [(0, 0), (1, 0), (0, 1), (2, 0)],
              [(0, 0), (0, 1), (0, 2), (-1, 2)],
              [(0, 0), (1, 0), (2, 0), (2, 1)],
              [(0, 0), (1, 0), (0, 1), (0, 2)],
              [(0, 0), (0, 1), (1, 1), (2, 1)],
              [(0, 0), (0, 1), (1, 1), (1, 2)], 
              [(0, 0), (1, 0), (1, -1), (2, -1)],
              [(0, 0), (1, 0), (1, 1), (2, 1)],
              [(0, 0), (0, 1), (-1, 1), (-1, 2)],
              [(0, 0), (1, 0), (1, -1), (2, 0)],
              [(0, 0), (0, 1), (-1, 1), (0, 2)],
              [(0, 0), (1, 0), (2, 0), (1, 1)],
              [(0, 0), (0, 1), (0, 2), (1, 1)]]


def DFS(row, col):
    max_total = 0

    for tetro in tetro_list:
        total = 0

        for way in tetro:
            if board[row+way[1]][col+way[0]] == -1:
                total = 0
                break
            total += board[row+way[1]][col+way[0]]

        max_total = max(max_total, total)
    return max_total

answer = 0

for row in range(1, N+1):
    for col in range(1, M+1):
        answer = max(answer, DFS(row, col))

print(answer)