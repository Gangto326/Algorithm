import sys

def solve():
    MAX_NUM = 1_000_000

    read = sys.stdin.readline
    N, M, R = map(int, read().split())
    item_list = list(map(int, read().split()))

    board = [[MAX_NUM] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                board[i][j] = 0

    for _ in range(R):
        start, end, cost = map(int, read().split())
        start -= 1
        end -= 1

        board[start][end] = min(board[start][end], cost)
        board[end][start] = min(board[end][start], cost)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]
                    board[j][i] = board[i][k] + board[k][j]

    answer = 0
    for i in range(N):
        total = 0

        for j in range(N):
            if board[i][j] <= M:
                total += item_list[j]
        
        answer = max(answer, total)
    print(answer)


if __name__ == "__main__":
    solve()