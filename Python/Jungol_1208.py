import sys

def solve():
    MAX_Value = 1_000_000
    read = sys.stdin.readline
    N = int(read())

    board = [[MAX_Value] * 52 for _ in range(52)]
    end_set = set()

    for _ in range(N):
        start, end, length = read().split()
        length = int(length)

        if not start.islower():
            start = ord(start) - 39
            end_set.add(start)
        else:
            start = ord(start) - 97
        
        if not end.islower():
            end = ord(end) - 39
            end_set.add(end)
        else:
            end = ord(end) - 97

        board[start][end] = min(board[start][end], length)
        board[end][start] = min(board[end][start], length)

    for k in range(52):
        for i in range(52):
            if board[i][k] == MAX_Value:
                continue

            for j in range(52):
                if i == j:
                    continue

                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]

    end_set.remove(ord('Z') - 39)
    answer, min_count = None, float('inf')
    for i in end_set:
        if min_count > board[i][-1]:
            answer = chr(i + 39)
            min_count = board[i][-1]

    print(answer, min_count)


if __name__ == "__main__":
    solve()