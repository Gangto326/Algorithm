import sys

def solve():
    read = sys.stdin.readline
    board = [list(map(int, list(read().rstrip()))) for _ in range(9)]

    check_box = [[0 for _ in range(3)] for _ in range(3)]
    check_row = [0 for _ in range(9)]
    check_col = [0 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                check_row[i] += 1 << board[i][j]
                check_col[j] += 1 << board[i][j]
                check_box[i//3][j//3] += 1 << board[i][j]

    flag = False
    def DFS(x, y):
        nonlocal board, check_box, check_col, check_row, flag
        if flag:
            return

        if x > 8:
            flag = True
            for i in range(9):
                row_string = ""
                for j in range(9):
                    row_string += str(board[i][j])
                
                print(row_string)
            return
        
        if board[x][y] != 0:
            DFS(x + ((y+1)//9), (y+1) % 9)
        
        else:
            for i in range(1, 10):
                mask = 1 << i
                if not check_box[x//3][y//3] & mask and not check_row[x] & mask and not check_col[y] & mask:
                    board[x][y] = i
                    check_box[x//3][y//3] += mask
                    check_row[x] += mask
                    check_col[y] += mask

                    DFS(x + ((y+1)//9), (y+1) % 9)

                    board[x][y] = 0
                    check_box[x//3][y//3] -= mask
                    check_row[x] -= mask
                    check_col[y] -= mask

    DFS(0, 0)


if __name__ == "__main__":
    solve()