import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    M, N = map(int, read().split())

    way_index = [1, 2, 4, 8]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    island_dict = dict()

    board = [list(map(int, read().split())) for _ in range(N)]
    check = [[0] * M for _ in range(N)]

    island = 0
    for row in range(N):
        for col in range(M):
            if check[row][col] == 0:
                island += 1

                BFS = deque()
                BFS.append((row, col))
                check[row][col] = island
                
                total = 1
                while BFS:
                    r, c = BFS.popleft()

                    for i in range(4):
                        if not (board[r][c] & way_index[i]):
                            nr, nc = r + dy[i], c + dx[i]

                            if 0 <= nr < N and 0 <= nc < M:
                                if check[nr][nc]:
                                    continue

                                check[nr][nc] = island
                                total += 1
                                BFS.append((nr, nc))

                island_dict[island] = total
    
    print(len(island_dict))
    answer = max(island_dict.values())
    print(answer)
    answer_row, answer_col, answer_wall = 0, 0, 0

    for col in range(M):
        for row in range(N-1, -1, -1):
            for i in range(1, 3):
                nr, nc = row + dy[i], col + dx[i]

                if 0 <= nr < N and 0 <= nc < M:
                    if check[row][col] != check[nr][nc]:
                        num = island_dict[check[row][col]] + island_dict[check[nr][nc]]

                        if answer < num:
                            answer = num
                            answer_row, answer_col, answer_wall = row + 1, col + 1, i
                            
    answer_wall = 'E' if answer_wall == 2 else 'N'
    print(answer)
    print(answer_row, answer_col, answer_wall)


if __name__ == "__main__":
    solve()