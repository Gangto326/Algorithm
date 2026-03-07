import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [[-1] * (N + 2)] + [[-1] + list(read().split()) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
    MAX_DP = [[-float('inf')] * (N + 2) for _ in range(N + 2)]
    MIN_DP = [[float('inf')] * (N + 2) for _ in range(N + 2)]

    operator_set = {'*', '-', '+'}

    def DFS(row, col, total, operator):
        if board[row][col] == -1:
            return

        if board[row][col] in operator_set:
            DFS(row + 1, col, total, board[row][col])
            DFS(row, col + 1, total, board[row][col])

        else:
            next_total = total
            current_num = int(board[row][col])

            if operator == '+':
                next_total += current_num
            elif operator == '-':
                next_total -= current_num
            else:
                next_total *= current_num

            flag = False
            
            if MAX_DP[row][col] < next_total:
                MAX_DP[row][col] = next_total
                flag = True
            
            if MIN_DP[row][col] > next_total:
                MIN_DP[row][col] = next_total
                flag = True
            
            if flag:
                DFS(row + 1, col, next_total, board[row][col])
                DFS(row, col + 1, next_total, board[row][col])


    DFS(1, 1, 0, '+')

    print(MAX_DP[N][N], MIN_DP[N][N])

if __name__ == "__main__":
    solve()