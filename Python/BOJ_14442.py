import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M, K = map(int, read().split())
    board = [list(map(int, list(read().rstrip()))) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    check = [[0] * M for _ in range(N)]
    BFS = deque()
    BFS.append((0, 0, 1, K))

    answer = -1
    while BFS:
        row, col, count, crush = BFS.popleft()
        
        if row == N-1 and col == M-1:
            answer = count
            break

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if board[nr][nc] == 1 and crush:
                next_crush = crush - 1

                if not check[nr][nc] & (1 << next_crush):
                    check[nr][nc] |= (1 << next_crush)
                    BFS.append((nr, nc, count + 1, next_crush))
            
            elif board[nr][nc] == 0 and not check[nr][nc] & (1 << crush):
                check[nr][nc] |= (1 << crush)
                BFS.append((nr, nc, count + 1, crush))

    print(answer)


if __name__ == "__main__":
    solve()