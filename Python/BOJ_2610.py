import sys

def solve():
    MAX_NUM = 10_000_000
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    DP = [[MAX_NUM] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = int(next(iterator)), int(next(iterator))
        DP[a][b] = 1
        DP[b][a] = 1
    
    for i in range(1, N + 1):
        DP[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
    
    check = set()
    answer_list = []
    for i in range(1, N + 1):
        if not i in check:
            group = []

            for j in range(1, N + 1):
                if DP[i][j] != MAX_NUM:
                    group.append(j)
            
            min_num = float('inf')
            index = 0
            for g in group:
                max_num = 0

                for j in range(1, N + 1):
                    if DP[g][j] != MAX_NUM:
                        max_num = max(max_num, DP[g][j])
            
                if max_num < min_num:
                    min_num = max_num
                    index = g

            answer_list.append(index)
            for g in group:
                check.add(g)

    answer_list.sort()
    print(len(answer_list))
    for answer in answer_list:
        print(answer)


if __name__ == "__main__":
    solve()