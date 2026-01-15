import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())

    board = [list(map(int, read().split())) for _ in range(N)]
    check_left = set()
    check_right = set()
    answer = 0
    max_count = 0

    white_bishop = []
    black_bishop = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i % 2 == j % 2:
                    white_bishop.append((i, j))
                else:
                    black_bishop.append((i, j))


    def DFS(index, count, color):
        nonlocal max_count, white_bishop, black_bishop, check_left, check_right

        bishops = []
        if color:
            bishops = white_bishop
        else:
            bishops = black_bishop

        if index >= len(bishops):
            max_count = max(max_count, count)
            return
        
        row, col = bishops[index]
        left = row-col
        right = row+col
        if not (left in check_left) and not (right in check_right):
            check_left.add(left)
            check_right.add(right)

            DFS(index+1, count+1, color)

            check_left.remove(left)
            check_right.remove(right)
        
        DFS(index+1, count, color)
        

    DFS(0, 0, 1)
    answer += max_count

    check_left = set()
    check_right = set()
    max_count = 0

    DFS(0, 0, 0)
    print(answer + max_count)


if __name__ == "__main__":
    solve()