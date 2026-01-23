import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    board = [[100] * (N+2)] + [[100] + list(map(int, read().split())) + [100] for _ in range(N)] + [[100] * (N+2)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    baby_shark = 2
    eat_count = 0
    shark_row, shark_col = 0, 0

    for row in range(1, N+1):
        for col in range(1, N+1):
            if board[row][col] == 9:
                shark_row, shark_col = row, col
                board[row][col] = 0
                break

    answer = 0
    while True:
        BFS = deque()
        BFS.append((shark_row, shark_col, 0))

        check = [[True] * (N+2) for _ in range(N+2)]
        check[shark_row][shark_col] = False

        flag = 500
        eat_row, eat_col = 100, 100
        while BFS:
            row, col, count = BFS.popleft()

            if count >= flag:
                break

            for way in range(4):
                nr, nc = row + dx[way], col + dy[way]

                if not check[nr][nc] or board[nr][nc] > baby_shark:
                    continue
                
                if board[nr][nc] != 0 and board[nr][nc] < baby_shark:
                    flag = count+1
                    check[nr][nc] = False

                    if eat_row > nr:
                        eat_row, eat_col = nr, nc
                    elif eat_row == nr and eat_col > nc:
                        eat_row, eat_col = nr, nc

                else:
                    BFS.append((nr, nc, count+1))
                    check[nr][nc] = False
                
        if flag == 500:
            break
        
        board[eat_row][eat_col] = 0
        shark_row, shark_col = eat_row, eat_col
        eat_count += 1

        if baby_shark == eat_count:
            baby_shark += 1
            eat_count = 0

        answer += flag

    print(answer)


if __name__ == "__main__":
    solve()