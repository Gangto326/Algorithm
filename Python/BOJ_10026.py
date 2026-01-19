import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    board = [['X'] * (N+2)] + [['X'] + list(read().rstrip()) + ['X'] for _ in range(N)] +[['X'] * (N+2)]
    RGB = [[0] * (N+2) for _ in range(N+2)]
    RB = [[0] * (N+2) for _ in range(N+2)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    answer = 1
    for row in range(1, N+1):
        for col in range(1, N+1):
            if RGB[row][col] == 0:
                BFS = deque()
                BFS.append((row, col, board[row][col]))
                RGB[row][col] = answer

                while BFS:
                    r, c, color = BFS.popleft()

                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]

                        if board[nr][nc] == color and RGB[nr][nc] == 0:
                            BFS.append((nr, nc, color))
                            RGB[nr][nc] = answer

                answer += 1
    
    answer2 = 1
    same_color = set()
    same_color.add("R")
    same_color.add("G")

    for row in range(1, N+1):
        for col in range(1, N+1):
            if RB[row][col] == 0:
                BFS = deque()
                BFS.append((row, col, board[row][col]))
                RB[row][col] = answer2

                while BFS:
                    r, c, color = BFS.popleft()

                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]

                        if ((board[nr][nc] == color) or (board[nr][nc] in same_color and color in same_color)) and RB[nr][nc] == 0:
                            BFS.append((nr, nc, color))
                            RB[nr][nc] = answer2

                answer2 += 1

    print(answer-1, answer2-1)
    

if __name__ == "__main__":
    solve()