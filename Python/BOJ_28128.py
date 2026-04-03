import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    board = [["MANIPULATED"] * (M + 2)] + [[next(iterator) for _ in range(M)] + ["MANIPULATED", "MANIPULATED"] for _ in range(N)] + [["MANIPULATED"] * (M + 2)]
    answer_set = set()

    N += 2
    M += 2

    for row in range(N):
        for col in range(M - 2):
            count_set = set()

            for i in range(3):
                if board[row][col + i] in count_set:
                    answer_set.add(board[row][col + i])
                else:
                    count_set.add(board[row][col + i])
    

    for row in range(N - 2):
        for col in range(M):
            count_set = set()

            for i in range(3):
                if board[row + i][col] in count_set:
                    answer_set.add(board[row + i][col])
                else:
                    count_set.add(board[row + i][col])
    
    if len(answer_set) == 1:
        print("MANIPULATED")
    else:
        answer_set.remove("MANIPULATED")
        answer_list = sorted(list(answer_set))

        for answer in answer_list:
            print(answer)


if __name__ == "__main__":
    solve()