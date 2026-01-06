import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, L, R = map(int, read().split())

    board = [[float('inf')] * (N+2)] + [[float('inf')] + list(map(int, read().split())) + [float('inf')] for _ in range(N)] + [[float('inf')] * (N+2)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    answer = 0
    while True:
        BFS = deque()
        check = [[True] * (N+2) for _ in range(N+2)]
        next_board = []

        flag = False
        for i in range(1, N+1):
            for j in range(1, N+1):
                if check[i][j]:
                    BFS.append((i, j))
                    check[i][j] = False

                    total = board[i][j]
                    merge_list = [(i, j)]
                    while BFS:
                        x, y = BFS.popleft()

                        for way in range(4):
                            nx, ny = x+dx[way], y+dy[way]

                            if check[nx][ny] and L <= abs(board[nx][ny]-board[x][y]) <= R:
                                check[nx][ny] = False
                                total += board[nx][ny]
                                merge_list.append((nx, ny))
                                BFS.append((nx, ny))
                    
                    if len(merge_list) > 1:
                        flag = True
                    
                    merge_total = int(total / len(merge_list))
                    for x, y in merge_list:
                        next_board.append((x, y, merge_total))

        if not flag:
            break

        answer += 1
        for x, y, merge_total in next_board:
            board[x][y] = merge_total

    print(answer)


if __name__ == "__main__":
    solve()