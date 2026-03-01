import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T, W = int(next(iterator)), int(next(iterator))
    DP = [[[0, 0] for _ in  range(T + 1)] for _ in range(W + 2)]

    for j in range(1, T + 1):
        num = int(next(iterator))

        for i in range(W + 1):
            one, two = DP[i][j - 1]

            DP[i][j][0] = max(DP[i][j][0], one + 1 if num == 1 else one)
            DP[i][j][1] = max(DP[i][j][1], two + 1 if num == 2 else two)

            DP[i + 1][j][0] = max(DP[i + 1][j][0], two + 1 if num == 1 else two)
            DP[i + 1][j][1] = max(DP[i + 1][j][1], one + 1 if num == 2 else one)

    answer = 0
    flag = True
    for i in range(W + 1):
        if flag:
            answer = max(answer, DP[i][-1][0])
        else:
            answer = max(answer, DP[i][-1][1])
        
        flag = not flag

    print(answer)


if __name__ == "__main__":
    solve()