import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    company_list = [[0] for _ in range(M + 1)]

    for _ in range(N):
        cost = int(next(iterator))

        for i in range(1, M + 1):
            company_list[i].append(int(next(iterator)))

    DP = [0] * (N + 1)
    check = [[] for _ in range(N + 1)]

    for i in range(1, M + 1):
        company = company_list[i]

        for k in range(N, 0, -1):
            for j in range(N, 0, -1):
                if k - j < 0:
                    continue

                if DP[k] < DP[k - j] + company[j]:
                    DP[k] = DP[k - j] + company[j]
                    check[k] = check[k - j][:]
                    check[k].append((i, j))

    print(DP[-1])
    answer_list = [0] * (M + 1)

    for company, cost in check[-1]:
        answer_list[company] = cost

    print(*answer_list[1:])


if __name__ == "__main__":
    solve()