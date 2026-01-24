import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [[0] * (M+2)] + [[0] + list(map(int, read().split())) + [0] for _ in range(N)] + [[0] * (M+2)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    air_zone = set()
    cheese_set = set()
    BFS = deque()

    for row in range(N+2):
        for col in range(M+2):
            if board[row][col] == 1:
                cheese_set.add((row, col))
                continue

            if row == 0 or row == N+1:
                if board[row][col] == 0:
                    BFS.append((row, col))
                    air_zone.add((row, col))
            
            else:
                if col == 0 or col == M+1:
                    if board[row][col] == 0:
                        BFS.append((row, col))
                        air_zone.add((row, col))
    
    while BFS:
        row, col = BFS.popleft()

        for way in range(4):
            nr, nc = row + dx[way], col + dy[way]

            if nr < 0 or nc < 0 or nr >= N+2 or nc >= M+2:
                continue

            if board[nr][nc] == 1:
                continue

            if not (nr, nc) in air_zone:
                BFS.append((nr, nc))
                air_zone.add((nr, nc))
    
    answer = 0
    while cheese_set:
        melting = set()
        answer += 1

        for row, col in cheese_set:
            count = 0
            
            for way in range(4):
                nr, nc = row + dx[way], col + dy[way]

                if (nr, nc) in air_zone:
                    count += 1
            
            if count >= 2:
                melting.add((row, col))
        
        BFS = deque()
        for row, col in melting:
            board[row][col] = 0
            cheese_set.remove((row, col))
            air_zone.add((row, col))
            BFS.append((row, col))

        while BFS:
            row, col = BFS.popleft()

            for way in range(4):
                nr, nc = row + dx[way], col + dy[way]

                if nr < 0 or nc < 0 or nr >= N+2 or nc >= M+2:
                    continue

                if board[nr][nc] == 1:
                    continue

                if not (nr, nc) in air_zone:
                    BFS.append((nr, nc))
                    air_zone.add((nr, nc))

    print(answer)


if __name__ == "__main__":
    solve()