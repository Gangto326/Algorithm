import sys
sys.setrecursionlimit(40_000)

def solve():
    read = sys.stdin.readline
    R, C = map(int, read().split())
    board = [['X'] * (C + 2)] + [['X'] + list(read().strip()) + ['X'] for _ in range(R)] + [['X'] * (C + 2)]
    bucket = [[(1, i)] for i in range(C + 1)]

    N = int(read())
    

    def DFS(index):
        root = bucket[index]

        while True:
            row, col = root[-1]

            if board[row][col] == ".":
                break

            root.pop()

        while True:
            row, col = root[-1]
            nr = row + 1

            if board[nr][col] == ".":
                root.append((nr, col))

            elif board[nr][col] == "X":
                board[row][col] = "O"
                break

            elif board[nr][col] == "O":
                if (board[row][col - 1] == ".") and (board[nr][col - 1] == "."):
                    root.append((nr, col - 1))
                
                elif (board[row][col + 1] == ".") and (board[nr][col + 1] == "."):
                    root.append((nr, col + 1))

                else:
                    board[row][col] = "O"
                    break

            
    for _ in range(N):
        query = int(read())
        DFS(query)

    for i in range(1, R + 1):
        print("".join(board[i][1:-1]))


if __name__ == '__main__':
    solve()