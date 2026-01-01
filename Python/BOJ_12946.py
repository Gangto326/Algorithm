import sys
sys.setrecursionlimit(100_000)
read = sys.stdin.readline
N = int(read().rstrip())

board = [[float('inf')] * (N+2)] + [[float('inf')] + [float('inf') if i == '-' else 0 for i in list(read().rstrip())] + [float('inf')] for _ in range(N)] + [[float('inf')] * (N+2)]

dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]

is_zero, is_one = True, True
for i in range(1, N+2):
    for j in range(1, N+2):
        if board[i][j] == 0:
            is_zero = False
            
            for way in range(6):
                nx, ny = i+dx[way], j+dy[way]

                if board[nx][ny] == 0:
                    is_one = False


def DFS(x, y, flag):
    global board
    board[x][y] = flag+1

    for way in range(6):
        nx, ny = x+dx[way], y+dy[way]

        if board[nx][ny] != float('inf'):
            if board[nx][ny] == 0:
                if not DFS(nx, ny, not flag):
                    return False
            
            elif board[nx][ny] == board[x][y]:
                return False

    return True

is_two = True
for i in range(1, N+2):
    if not is_two:
        break

    for j in range(1, N+2):
        if board[i][j] == 0:
            if not DFS(i, j, False):
                is_two = False
                break

if is_zero: print(0)
elif is_one: print(1)
elif is_two: print(2)
else: print(3)