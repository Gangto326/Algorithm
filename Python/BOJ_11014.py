import sys
sys.setrecursionlimit(10_000)

def solve():
    read = sys.stdin.readline
    T = int(read())
    dx = [1, 0, -1, 1, 0, -1]
    dy = [-1, -1, -1, 1, 1, 1]

    for tc in range(T):
        N, M = map(int, read().split())
        board = [list(read().strip()) for _ in range(N)]
        matched = [[(-1, -1)] * M for _ in range(N)]


        def DFS(row, col):
            for i in range(6):
                nr, nc = row + dx[i], col + dy[i]

                if 0 <= nr < N and 0 <= nc < M:
                    if not check[nr][nc]:
                        continue
                    
                    check[nr][nc] = False

                    if board[nr][nc] == '.' and (matched[nr][nc] == (-1, -1) or DFS(matched[nr][nc][0], matched[nr][nc][1])):
                        matched[nr][nc] = (row, col)
                        return True
                
            return False
            
        
        answer = 0
        for row in range(N):
            for col in range(M):
                if col % 2 == 0 and board[row][col] == '.':
                    check = [[True] * M for _ in range(N)]

                    if DFS(row, col):
                        answer += 1

        total = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == '.':
                    total += 1

        print(total - answer)


if __name__ == "__main__":
    solve()