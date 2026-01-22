import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    board = [['2'] * (M+2)] + [['2'] + list(read().rstrip()) + ['2'] for _ in range(N)] + [['2'] * (M+2)]
    check = [[[True, True] for _ in range(M+2)] for _ in range(N+2)]

    BFS = deque()
    BFS.append((1, 1, 1, 0))

    answer = -1
    while BFS:
        row, col, count, chance = BFS.popleft()

        if row == N and col == M:
            answer = count
            break

        for way in range(4):
            nr, nc = row + dx[way], col + dy[way]

            if board[nr][nc] == '0' and check[nr][nc][chance]:
                check[nr][nc][chance] = False
                BFS.append((nr, nc, count+1, chance))
            
            elif board[nr][nc] == '1' and chance == 0 and check[nr][nc][1]:
                check[nr][nc][1] = False
                BFS.append((nr, nc, count+1, 1))

    print(answer)


if __name__ == "__main__":
    solve()