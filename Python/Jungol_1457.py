import sys
from collections import deque

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    R, C, N = int(next(iterator)), int(next(iterator)), int(next(iterator))
    board = [[0] * C for _ in range(R)]

    for _ in range(N):
        x1, y1, x2, y2 = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))

        board[max(y1, y2) - 1][min(x1, x2)] += 1

        if max(x1, x2) < C:
            board[max(y1, y2) - 1][max(x1, x2)] -= 1

        if min(y1, y2) > 0:
            board[min(y1, y2) - 1][min(x1, x2)] -= 1
        
        if (min(y1, y2) > 0) and (max(x1, x2) < C):
            board[min(y1, y2) - 1][max(x1, x2)] += 1
        
    for row in range(R):
        for col in range(1, C):
            board[row][col] += board[row][col - 1]
    
    for col in range(C):
        for row in range(R - 2, -1, -1):
            board[row][col] += board[row + 1][col]

    
    cheak = [[True] * C for _ in range(R)]
    answer_list = []
    for row in range(R):
        for col in range(C):
            if (board[row][col] == 0) and cheak[row][col]:
                BFS = deque()
                BFS.append((row, col))

                cheak[row][col] = False
                count = 1

                while BFS:
                    r, c = BFS.popleft()
                    
                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]

                        if (0 <= nr < R) and (0 <= nc < C):
                            if (board[nr][nc] == 0) and cheak[nr][nc]:
                                cheak[nr][nc] = False
                                count += 1
                                BFS.append((nr, nc))
                
                answer_list.append(count)

    answer_list.sort()
    print(len(answer_list))
    print(*answer_list)


if __name__ == "__main__":
    solve()