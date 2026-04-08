import sys

def solve():
    read = sys.stdin.buffer.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    num_list = [0] + [int(next(iterator)) for _ in range(N)]
    board = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        start, end, cost = int(next(iterator)), int(next(iterator)), int(next(iterator))

        if start == N + 1:
            start = 0
        if end == N + 1:
            end = 0

        board[start][end] = min(board[start][end], cost)
    
    ALL_VISITED = 1 << (N + 1)
    DP = [[float('inf')] * ALL_VISITED for _ in range(N + 1)]
    DP[0][1] = 0

    for visited in range(1, ALL_VISITED):
        if not visited & 1:
            continue

        for i in range(N + 1):
            if not visited & (1 << i):
                continue

            if not visited & (1 << num_list[i]):
                continue

            prev_visited = visited ^ (1 << i)

            for j in range(N + 1):
                if i == j:
                    continue

                if not prev_visited & (1 << j):
                    continue
                
                if board[j][i] == float('inf'):
                    continue

                if DP[j][prev_visited] == float('inf'):
                    continue

                DP[i][visited] = min(DP[i][visited], DP[j][prev_visited] + board[j][i])
    
    answer = float('inf')
    for i in range(N + 1):
        answer = min(answer, DP[i][ALL_VISITED - 1] + board[i][0])
    
    print(answer if answer != float('inf') else -1)


if __name__ == "__main__":
    solve()