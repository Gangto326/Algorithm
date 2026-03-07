import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [[-1] * (N + 2)] + [[-1] + list(map(int, read().split())) + [-1] for _ in range(N)] +[[-1] * (N + 2)]
    DP = [[[float('inf')] * (N * 2) for _ in range(N + 2)] for _ in range(N + 2)]


    def DFS(row, col, total, last_num):

        if board[row][col] == -1:
            return

        if board[row][col] > last_num:
            next_total = total + 1
            next_num = board[row][col]

            if next_num < DP[row][col][next_total]:
                DP[row][col][next_total] = next_num
                DFS(row + 1, col, next_total, next_num)
                DFS(row, col + 1, next_total, next_num)

        if last_num < DP[row][col][total]:
            DP[row][col][total] = last_num
            DFS(row + 1, col, total, last_num)
            DFS(row, col + 1, total, last_num)


    DFS(1, 1, 0, 0)

    answer = 0
    for i in range(N * 2):
        if DP[N][N][i] != float('inf'):
            answer = max(answer, i)
    
    print(answer)


if __name__ == "__main__":
    solve()