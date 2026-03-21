import sys
sys.setrecursionlimit(20_000)

def solve():
    read = sys.stdin.readline
    R, C = map(int, read().split())

    board = [list(read().strip()) for _ in range(R)]
    parents = [i for i in range(R * C)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]


    def find(u):
        if parents[u] == u:
            return u
        parents[u] = find(parents[u])
        return parents[u]


    def union(u, v):
        pu = find(u)
        pv = find(v)

        if pu == pv:
            return False
        
        parents[pv] = pu
        return True


    def go(row, col):
        u = row * C + col 

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == '.':
                    v = nr * C + nc
                    union(u, v)


    waters = []
    swan_list = []
    for row in range(R):
        for col in range(C):
            if board[row][col] == 'X':
                continue
            
            if board[row][col] == 'L':
                swan_list.append((row, col))
                board[row][col] = '.'
            
            waters.append((row, col))
            go(row, col)

    answer = 0

    swan1_idx = swan_list[0][0] * C + swan_list[0][1]
    swan2_idx = swan_list[1][0] * C + swan_list[1][1]

    if find(swan1_idx) == find(swan2_idx):
        print(answer)
        return

    while True:
        next_waters = []

        while waters:
            row, col = waters.pop()

            for i in range(4):
                nr, nc = row + dx[i], col + dy[i]

                if 0 <= nr < R and 0 <= nc < C:
                    if board[nr][nc] == 'X':
                        next_waters.append((nr, nc))
                        board[nr][nc] = '.'
        
        for row, col in next_waters:
            go(row, col)

        waters = next_waters
        answer += 1

        if find(swan1_idx) == find(swan2_idx):
            print(answer)
            break
        

if __name__ == "__main__":
    solve()