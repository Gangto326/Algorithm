import sys, math

def solve():
    MAX_VALUE = 100_000_000
    read = sys.stdin.readline
    N = int(read())
    END = (1 << N) - 1
    
    board = [[MAX_VALUE] * N for _ in range(N)]
    node_list = []
    DP = [[MAX_VALUE] * N for _ in range(1 << N)]

    for _ in range(N):
        x, y = map(int, read().split())
        node_list.append((x, y))
    
    for i in range(N):
        for j in range(i, N):
            length = math.sqrt((node_list[i][0] - node_list[j][0]) ** 2 + (node_list[i][1] - node_list[j][1]) ** 2)
            board[i][j] = min(board[i][j], length)
            board[j][i] = min(board[j][i], length)
    
    DP[1][0] = 0

    for mask in range(1, 1 << N):
        for i in range(N):
            if not (mask & (1 << i)):
                continue

            before_mask = mask - (1 << i)
            if before_mask == 0:
                continue
            
            for j in range(N):
                if (before_mask & (1 << j)):
                    if DP[before_mask][j] + board[j][i] < DP[mask][i]:
                        DP[mask][i] = DP[before_mask][j] + board[j][i]
                        
    answer = MAX_VALUE
    for i in range(1, N):
        if DP[END][i] != MAX_VALUE:
            answer = min(answer, DP[END][i] + board[i][0])

    print(answer)

if __name__ == "__main__":
    solve()