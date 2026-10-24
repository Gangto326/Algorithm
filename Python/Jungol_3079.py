import sys
sys.setrecursionlimit(200_000)

def solve():
    read = sys.stdin.read()
    iterator = iter(read.split())
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    N, K = int(next(iterator)), int(next(iterator))
    parents = [i for i in range(K + 1)]
    union_count = 1


    def find(index):
        nonlocal parents

        if parents[index] == index:
            return index

        parents[index] = find(parents[index])
        return parents[index]


    def union(first, sec):
        fp = find(first)
        sp = find(sec)

        if fp == sp:
            return False
        
        parents[sp] = fp
        return True


    board = [[0] * N for _ in range(N)]
    start_map = []
    for i in range(1, K+1):
        row, col = int(next(iterator)) - 1, int(next(iterator)) - 1
        start_map.append((row, col))
        board[row][col] = i

        for j in range(4):
            nr, nc = row + dx[j], col + dy[j]

            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != 0 and board[nr][nc] != i:
                    if union(i, board[nr][nc]):
                        union_count += 1
    
    answer = 0
    while union_count != K:
        next_map = []

        for r, c in start_map:
            index = board[r][c]

            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]

                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == 0:
                        board[nr][nc] = index
                        next_map.append((nr, nc))

                        for j in range(4):
                            nnr, nnc = nr + dx[j], nc + dy[j]
                            
                            if 0 <= nnr < N and 0 <= nnc < N:
                                if board[nnr][nnc] != 0 and board[nnr][nnc] != index:
                                    if union(index, board[nnr][nnc]):
                                        union_count += 1
        
        start_map = next_map
        answer += 1

    print(answer)


if __name__ == "__main__":
    solve()