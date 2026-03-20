import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    move_dict = {1: (0, -1), 2: (-1, 0), 4: (0, 1), 8: (1, 0)}

    board = [list(map(int, read().split())) for _ in range(M)]
    check = [[0] * (N) for _ in range(M)]

    island_dict = {}

    island = 1
    for row in range(M):
        for col in range(N):
            if not check[row][col]:
                count = 1

                BFS = deque()
                BFS.append((row, col))
                check[row][col] = island

                while BFS:
                    r, c = BFS.popleft()

                    if not board[r][c] & 1:
                        wr, wc = move_dict[1]
                        nr, nc = r + wr, c + wc

                        if 0 <= nr < M and 0 <= nc < N:
                            if not check[nr][nc]:
                                BFS.append((nr, nc))
                                count += 1
                                check[nr][nc] = island

                    if not board[r][c] & 2:
                        wr, wc = move_dict[2]
                        nr, nc = r + wr, c + wc

                        if 0 <= nr < M and 0 <= nc < N:
                            if not check[nr][nc]:
                                BFS.append((nr, nc))
                                count += 1
                                check[nr][nc] = island
                    
                    if not board[r][c] & 4:
                        wr, wc = move_dict[4]
                        nr, nc = r + wr, c + wc

                        if 0 <= nr < M and 0 <= nc < N:
                            if not check[nr][nc]:
                                BFS.append((nr, nc))
                                count += 1
                                check[nr][nc] = island
                    
                    if not board[r][c] & 8:
                        wr, wc = move_dict[8]
                        nr, nc = r + wr, c + wc

                        if 0 <= nr < M and 0 <= nc < N:
                            if not check[nr][nc]:
                                BFS.append((nr, nc))
                                count += 1
                                check[nr][nc] = island

                island_dict[island] = count
                island += 1

    print(len(island_dict))

    answer = max(island_dict.values())
    print(answer)
    for row in range(M):
        for col in range(N):
            if row + 1 < M and check[row][col] != check[row + 1][col]:
                answer = max(answer, island_dict[check[row][col]] + island_dict[check[row + 1][col]])
            
            if col + 1 < N and check[row][col] != check[row][col + 1]:
                answer = max(answer, island_dict[check[row][col]] + island_dict[check[row][col + 1]])

    print(answer)


if __name__ == "__main__":
    solve()