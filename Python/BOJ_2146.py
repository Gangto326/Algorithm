import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [list(map(int, read().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    island_list = []

    mark = 2
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                island = set()

                BFS = deque()
                BFS.append((row, col))
                board[row][col] = mark

                while BFS:
                    r, c = BFS.popleft()

                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]

                        if nr < 0 or nc < 0 or nr >= N or nc >= N:
                            continue

                        if board[nr][nc] == 1:
                            board[nr][nc] = mark
                            BFS.append((nr, nc))
                        
                        elif board[nr][nc] == 0:
                            island.add((r, c))

                island_list.append(island)

    answer = float('inf')
    for i in range(len(island_list)-1):
        start_set = island_list[i]

        for j in range(i+1, len(island_list)):
            end_set = island_list[j]

            for x, y in start_set:
                for x2, y2 in end_set:
                    answer = min(answer, abs(x - x2) + abs(y - y2) - 1)
    
    print(answer)


if __name__ == "__main__":
    solve()