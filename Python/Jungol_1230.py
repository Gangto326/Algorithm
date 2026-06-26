import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    N = int(read())
    board = [[1] * (N + 2)] + [[1] + list(map(int, read().split())) + [1] for _ in range(N)] + [[1] * (N + 2)]
    answer = -1

    check = [[True] * (N + 2) for _ in range(N + 2)]
    check[1][1] = False


    def get_reachable(r, c):
        q = deque([(r, c)])
        visited = [[False] * (N + 2) for _ in range(N + 2)]
        visited[r][c] = True
        
        can_end = False
        possible_gifts = 0

        while q:
            curr_r, curr_c = q.popleft()
            
            if curr_r == N and curr_c == N:
                can_end = True
                
            for i in range(4):
                nr, nc = curr_r + dx[i], curr_c + dy[i]

                if check[nr][nc] and board[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = True

                    if board[nr][nc] == 2:
                        possible_gifts += 1

                    q.append((nr, nc))
                    
        return can_end, possible_gifts


    def DFS(row, col, count):
        nonlocal N, board, dx, dy, answer, check

        if row == N and col == N:
            answer = max(answer, count)
            return

        can_end, possible_gifts = get_reachable(row, col)
        
        if not can_end:
            return
            
        if count + possible_gifts <= answer:
            return

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if board[nr][nc] == 1:
                continue

            else:
                if check[nr][nc]:
                    check[nr][nc] = False
                    
                    if board[nr][nc] == 2:
                        DFS(nr, nc, count + 1)
                    else:
                        DFS(nr, nc, count)
                        
                    check[nr][nc] = True


    DFS(1, 1, int(bool(board[1][1] == 2)))

    print(answer)

if __name__ == "__main__":
    solve()