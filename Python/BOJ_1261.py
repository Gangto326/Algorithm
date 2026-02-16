import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [[1] * (N+2)] + [[1] + list(map(int, list(read().rstrip()))) + [1] for _ in range(M)] + [[1] * (N+2)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    BFS = deque()
    BFS.append((1, 1, 0))
    check = [[False] * (N+2)] + [[False] + [True] * N + [False] for _ in range(M)] +[[False] * (N+2)]

    while BFS:
        row, col, count = BFS.popleft()

        if row == M and col == N:
            print(count)
            return

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if check[nr][nc]:
                check[nr][nc] = False

                if board[nr][nc] == 1:
                    BFS.append((nr, nc, count + 1))
                else:
                    BFS.appendleft((nr, nc, count))


if __name__ == "__main__":
    solve()