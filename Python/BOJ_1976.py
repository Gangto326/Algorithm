import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    M = int(read())
    board = [list(map(int, read().split())) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    board[i][j] = 1
                    continue

                if not board[i][j]:
                    if board[i][k] and board[k][j]:
                        board[i][j] = 1
    
    num_list = list(map(int, read().split()))
    start = num_list[0] - 1

    for i in range(1, M):
        end = num_list[i]-1
        if not board[start][end]:
            print("NO")
            return
            
        start = end

    print("YES")


if __name__ == "__main__":
    solve()