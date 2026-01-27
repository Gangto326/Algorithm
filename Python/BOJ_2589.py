import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    R, C = map(int, read().split())

    board = [['W'] * (C+2)] + [['W'] + list(read().rstrip()) + ['W'] for _ in range(R)] + [['W'] * (C+2)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    
    answer = 0
    for row in range(1, R+1):
        for col in range(1, C+1):
            if board[row][col] == 'L':
                check = [[True] * (C+2) for _ in range(R+2)]
                check[row][col] = False

                BFS = deque()
                BFS.append((row, col, 0))

                while BFS:
                    r, c, count = BFS.popleft()
                    answer = max(answer, count)

                    count += 1
                    for way in range(4):
                        nr, nc = r+dx[way], c+dy[way]

                        if board[nr][nc] == 'W':
                            continue

                        if not check[nr][nc]:
                            continue
                        
                        check[nr][nc] = False
                        BFS.append((nr, nc, count))

    print(answer)


if __name__ == "__main__":
    solve()