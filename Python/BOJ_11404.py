import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    board = [[float('inf') if i != j else 0 for i in range(N)] for j in range(N)]

    query_num = int(read().rstrip())
    for _ in range(query_num):
        start, end, cost = map(int, read().split())
        start -= 1
        end -= 1
        board[start][end] = min(board[start][end], cost)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]

    for i in range(N):
        for j in range(N):
            if board[i][j] == float('inf'):
                board[i][j] = 0

    for answer in board:
        print(*answer)
        

if __name__ == "__main__":
    solve()