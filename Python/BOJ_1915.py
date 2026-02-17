import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [list(map(int, list(read().rstrip()))) for _ in range(N)]

    dx = [-1, 0, -1]
    dy = [0, -1, -1]

    for row in range(1, N):
        for col in range(1, M):
            if board[row][col] > 0:
                min_size = min([board[row + dx[i]][col + dy[i]] for i in range(3)])
                board[row][col] = min_size + 1

    answer = 0
    for b in board:
        answer = max(answer, max(b)**2)

    print(answer)


if __name__ == "__main__":
    solve()