import sys
sys.setrecursionlimit(10**6)

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    move_dict = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    board = [['X'] * (M+2)] + [['X'] + list(read().rstrip()) + ['X'] for _ in range(N)] + [['X'] * (M+2)]

    check = [[0] * (M+2) for _ in range(N+2)]
    answer = 0


    def DFS(row, col, stamp):
        nonlocal answer, check, board, move_dict

        if check[row][col]:
            if check[row][col] == stamp:
                answer += 1
            return
        
        if board[row][col] == 'X':
            return
        
        dr, dc = move_dict[board[row][col]]
        check[row][col] = stamp
        DFS(row + dr, col + dc, stamp)


    stamp_num = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if not check[i][j]:
                DFS(i, j, stamp_num)
                stamp_num += 1
    
    print(answer)


if __name__ == "__main__":
    solve()