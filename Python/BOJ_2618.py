import sys

def solve():
    read = sys.stdin.buffer.readline
    N = int(read())
    W = int(read())
    case_list = [[0, 0]] + [list(map(int, read().split())) for _ in range(W)]
    DP = [[float('inf')] * (W + 1) for _ in range(W + 1)]
    DP[0][0] = 0
    memo = [[(0, 0)] * (W + 1) for _ in range(W + 1)]


    def calculate(case_index, next_case, flag):
        nonlocal N

        x, y = case_list[case_index]
        nx, ny = case_list[next_case]

        if case_index == 0:
            if flag == 1:
                x, y = 1, 1
            else:
                x, y = N, N

        return abs(x - nx) + abs(y - ny)


    for i in range(W):
        for j in range(W):
            if i == j and i != 0:
                continue

            next_case = max(i, j) + 1

            cost = DP[i][j] + calculate(i, next_case, 1)
            if DP[next_case][j] > cost:
                DP[next_case][j] = cost
                memo[next_case][j] = (i, j)

            cost = DP[i][j] + calculate(j, next_case, 2)
            if DP[i][next_case] > cost:
                DP[i][next_case] = cost
                memo[i][next_case] = (i, j)
    
    min_cost = float('inf')
    last_x, last_y = 0, 0
    count = W

    for i in range(W):
        if DP[i][W] < min_cost:
            min_cost = DP[i][W]
            last_x, last_y = i, W
        
        if DP[W][i] < min_cost:
            min_cost = DP[W][i]
            last_x, last_y = W, i
    
    print(min_cost)
    answer_list = []
    while (last_x != 0) or (last_y != 0):
        if last_x == count:
            answer_list.append("1")
        elif last_y == count:
            answer_list.append("2")

        last_x, last_y = memo[last_x][last_y]
        count -= 1

    print("\n".join(reversed(answer_list)))


if __name__ == "__main__":
    solve()