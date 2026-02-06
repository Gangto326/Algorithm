import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M, K = map(int, read().split())
    board = [list(map(int, list(read().rstrip()))) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    check = [[[0] * M for _ in range(N)], [[0] * M for _ in range(N)]]
    
    BFS = deque()
    BFS.append((0, 0, 1, K, 0))
    check[0][0][0] |= 1 << 10

    answer = -1
    while BFS:
        row, col, count, k, time = BFS.popleft()

        if row == N-1 and col == M-1:
            answer = count
            break

        next_time = (time + 1) % 2
        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            
            if time == 1:
                if check[next_time][nr][nc] & (1 << k):
                   continue
               
                if board[nr][nc] == 1:
                    continue
               
                else:
                    check[next_time][nr][nc] |= (1 << k)
                    BFS.append((nr, nc, count + 1, k, next_time))
            
            else:
                next_check = k

                if board[nr][nc] == 1:
                    if not next_check:
                        continue

                    next_check -= 1
                
                if check[next_time][nr][nc] & (1 << next_check):
                    continue
                
                else:
                    check[next_time][nr][nc] |= (1 << next_check)
                    BFS.append((nr, nc, count + 1, next_check, next_time))
        

        if not check[next_time][row][col] & (1 << k):
            check[next_time][row][col] |= (1 << k)
            BFS.append((row, col, count + 1, k, next_time))

    print(answer)


if __name__ == "__main__":
    solve()