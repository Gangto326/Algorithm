import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [[1] * (N + 2)] + [[1] + list(map(int, read().split())) + [1] for _ in range(N)] + [[1] * (N + 2)]
    DP = [[[0] * (N + 2) for _ in range(N + 2)] for _ in range(3)]
    
    DP[0][1][2] = 1

    dx = [0, 1, 1]
    dy = [1, 0, 1]

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            for i in range(3):
                nr, nc = row + dx[i], col + dy[i]

                if board[nr][nc] != 1 and i == 0:
                    DP[i][nr][nc] += DP[0][row][col] + DP[2][row][col]

                elif board[nr][nc] != 1 and i == 1:
                    DP[i][nr][nc] += DP[1][row][col] + DP[2][row][col]

                elif board[nr][nc] != 1 and board[nr-1][nc] != 1 and board[nr][nc-1] != 1 and i == 2:
                    DP[i][nr][nc] += DP[0][row][col] + DP[1][row][col] + DP[2][row][col]
    

    print(DP[0][N][N] + DP[1][N][N] + DP[2][N][N])


if __name__ == "__main__":
    solve()