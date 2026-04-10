import sys
from collections import deque

def solve():
    read = sys.stdin.buffer.readline
    N, M = map(int, read().split())
    node_list = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for _ in range(M):
        ax, ay, bx, by = map(int, read().split())
        node_list[ax][ay].append((bx, by))
    
    check = [[False] * (N + 1) for _ in range(N + 1)]
    on_off = [[False] * (N + 1) for _ in range(N + 1)]
    check[1][1] = True
    on_off[1][1] = True

    BFS = deque()
    BFS.append((1, 1))
    answer = 1

    while BFS:
        row, col = BFS.popleft()

        for nx, ny in node_list[row][col]:

            if not on_off[nx][ny]:
                on_off[nx][ny] = True
                answer += 1
                
                for i in range(4):
                    nnx, nny = nx + dx[i], ny + dy[i]

                    if 0 < nnx <= N and 0 < nny <= N and check[nnx][nny]:
                        check[nx][ny] = True
                        BFS.append((nx, ny))
                        break
        
        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if 0 < nr <= N and 0 < nc <= N:
                if on_off[nr][nc] and not check[nr][nc]:
                    check[nr][nc] = True
                    BFS.append((nr, nc))

    print(answer)
    

if __name__ == "__main__":
    solve()