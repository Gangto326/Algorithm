import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    DP = [[-float('inf')] * N for _ in range(2)]
    DP[0][0] = num_list[0]
    DP[1][0] = -float('inf')

    answer = DP[0][0]
    for i in range(1, N):
        num = num_list[i]

        DP[0][i] = max(DP[0][i-1] + num, num)
        DP[1][i] = max(DP[1][i-1] + num, DP[0][i-1])
        answer = max(answer, DP[0][i], DP[1][i])

    print(answer)


if __name__ == '__main__':
    solve()