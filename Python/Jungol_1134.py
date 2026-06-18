import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    T = int(read())
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for test_case in range(T):
        K = int(read())
        R, C = map(int, read().split())
        board = [list(read().strip().replace(" ", "")) for _ in range(R)]

        start_r, start_c = -1, -1
        for row in range(R):
            for col in range(C):
                if board[row][col] == "S":
                    start_r, start_c = row, col
                    board[row][col] = "."
                    break

            if start_r != -1:
                break
        
        BFS = deque()
        BFS.append((start_r, start_c, 0))

        check = [[True] * C for _ in range(R)]
        check[start_r][start_c] = False
        flag = False

        while BFS:
            r, c, k = BFS.popleft()

            if k > K:
                continue

            if board[r][c] == "T":
                flag = True
                break

            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]

                if 0 <= nr < R and 0 <= nc < C:
                    if not check[nr][nc]:
                        continue
                    
                    check[nr][nc] = False
                    if board[nr][nc] == "*":
                        BFS.append((nr, nc, k + 1))
                    
                    else:
                        BFS.appendleft((nr, nc, k))
        
        if flag:
            print("y")
        else:
            print("n")


if __name__ == "__main__":
    solve()