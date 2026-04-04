import sys

def solve():
    read = sys.stdin.readline
    R, C = map(int, read().split())
    board = [list(read().strip()) for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if board[row][col] == ".":
                board[row][col] = 1
            else:
                board[row][col] = 0
    
    for row in range(R):
        for col in range(C - 1):
            if board[row][col + 1]:
                board[row][col + 1] += board[row][col]
    
    answer = 0
    for col in range(C):
        for row in range(R):
            if board[row][col]:
                min_col = float('inf')
                row_count = 0

                for i in range(row, R):
                    min_col = min(min_col, board[i][col])
                    row_count += 1
                    
                    if min_col == 0:
                        break

                    answer = max(answer, min_col * 2 + row_count * 2 - 1)

    print(answer)


if __name__ == "__main__":
    solve()