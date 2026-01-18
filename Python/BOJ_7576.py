import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    M, N = map(int, read().split())
    board = [[-1] * (M+1)] + [[-1] + list(map(int, read().split())) + [-1] for _ in range(N)] + [[-1] * (M+1)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    BFS = deque()
    for row in range(1, N+1):
        for col in range(1, M+1):
            if board[row][col] == 1:
                BFS.append((row, col, 1))
    
    answer = 0
    while BFS:
        row, col, days = BFS.popleft()
        flag = False

        for way in range(4):
            nr, nc = row + dx[way], col + dy[way]

            if board[nr][nc] == 0:
                board[nr][nc] = 1
                flag = True
                BFS.append((nr, nc, days + 1))
        
        if flag:
            answer = days

    for row in range(1, N+1):
        if answer == -1:
            break

        for col in range(1, M+1):
            if board[row][col] == 0:
                answer = -1
                break
    
    print(answer)


if __name__ == "__main__":
    solve()