import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    dessert_list = [list(map(int, read().split())) for _ in range(M)]

    if M == 1:
        answer = dessert_list[0][0]

        for i in range(1, N):
            answer += dessert_list[0][i] // 2
            
        print(answer)
        return

    DP = [[0] * (N + 1) for _ in range(M)]
    for i in range(1, N + 1):
        one_index = 0
        two_index = 1

        if DP[1][i - 1] > DP[0][i - 1]:
            one_index, two_index = 1, 0

        for j in range(2, M):
            if DP[j][i - 1] > DP[one_index][i - 1]:
                two_index = one_index
                one_index = j

            elif DP[j][i - 1] > DP[two_index][i - 1]:
                two_index = j
        
        for j in range(M):
            dessert = dessert_list[j][i - 1]

            if one_index == j:
                DP[j][i] = max(DP[j][i], DP[one_index][i - 1] + (dessert // 2), DP[two_index][i - 1] + dessert)
            else:
                DP[j][i] = max(DP[j][i], DP[one_index][i - 1] + dessert)

    answer = 0
    for li in DP:
        answer = max(answer, li[-1])
    print(answer)


if __name__ == "__main__":
    solve()