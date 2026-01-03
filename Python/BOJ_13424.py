import sys

read = sys.stdin.readline
T = int(read().rstrip())

for tc in range(T):
    N, M = map(int, read().split())
    board = [[5_000_000] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        board[i][i] = 0
    
    for _ in range(M):
        a, b, c = map(int, read().split())
        board[a][b] = min(board[a][b], c)
        board[b][a] = min(board[b][a], c)

    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if board[j][k] > board[j][i] + board[i][k]:
                    board[j][k] = board[j][i] + board[i][k]

    K = int(read().rstrip())
    students = list(map(int, read().split()))

    answer = 0
    total = float('inf')
    for i in range(1, N+1):
        min_length = 0

        for student in students:
            min_length += board[student][i]
        
        if total > min_length:
            answer = i
            total = min_length
    
    print(answer)