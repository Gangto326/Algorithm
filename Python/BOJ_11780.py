import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    M = int(next(iterator))

    board = [[float('inf')] * N for _ in range(N)]
    check = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        start, end, cost = int(next(iterator)), int(next(iterator)), int(next(iterator))

        if board[start-1][end-1] > cost:
            board[start-1][end-1] = cost
            check[start-1][end-1] = [start]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    board[i][j] = 0
                    board[j][i] = 0
                
                else:
                    if board[i][j] > board[i][k] + board[k][j]:
                        board[i][j] = board[i][k] + board[k][j]
                        check[i][j] = check[i][k] + check[k][j]

    for i in range(N):
        for j in range(N):
            if board[i][j] == float('inf'):
                board[i][j] = 0

    for b in board:
        print(*b)

    for i in range(N):
        for j in range(N):
            if len(check[i][j]):
                print(len(check[i][j]) + 1, *check[i][j], j + 1)
            
            else:
                print(0)


if __name__ == "__main__":
    solve()