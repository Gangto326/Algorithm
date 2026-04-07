import sys

def solve():
    read = sys.stdin.buffer.readline
    N = int(read())
    board = [list(map(int, read().split())) for _ in range(N)]
    
    ALL_VISITED = 1 << N
    DP = [[float('inf')] * ALL_VISITED for _ in range(N)]
    DP[0][1] = 0
    parents = [[-1] * ALL_VISITED for _ in range(N)]

    max_count = 0
    memo_index = 0
    memo_visited = 0
    
    for visited in range(1, ALL_VISITED):
        if not visited & 1:
            continue

        for i in range(N):
            if not visited & (1 << i):
                continue

            prev_visited = visited ^ (1 << i)

            for j in range(N):
                if i == j:
                    continue

                if not prev_visited & (1 << j):
                    continue

                if not board[j][i]:
                    continue

                if DP[i][visited] > DP[j][prev_visited] + 1:
                    DP[i][visited] = DP[j][prev_visited] + 1
                    parents[i][visited] = j

                    if max_count < DP[i][visited]:
                        max_count = DP[i][visited]
                        memo_index = i
                        memo_visited = visited

    answer_list = []
    answer_list.append(memo_index + 1)

    while memo_index:
        answer_list.append(parents[memo_index][memo_visited] + 1)
        memo_visited -= (1 << memo_index)
        memo_index = answer_list[-1] - 1

    print(max_count + 1)
    print(*reversed(answer_list))


if __name__ == "__main__":
    solve()