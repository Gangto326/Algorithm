import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    word_list = [read().strip() for _ in range(N)]
    
    ALL_VISITED = 1 << N
    DP = [[-1] * ALL_VISITED for _ in range(N)]
    
    for i in range(N):
        DP[i][1 << i] = len(word_list[i])

    for visited in range(1, ALL_VISITED):
        for i in range(N):
            if not visited & (1 << i):
                continue

            prev_visited = visited ^ (1 << i)

            for j in range(N):
                if i == j:
                    continue

                if not visited & (1 << j):
                    continue

                if DP[j][prev_visited] == -1:
                    continue

                if word_list[j][-1] != word_list[i][0]:
                    continue

                DP[i][visited] = max(DP[i][visited], DP[j][prev_visited] + len(word_list[i]))

    answer = 0
    for dp in DP:
        answer = max(answer, max(dp))
    
    print(answer)


if __name__ == "__main__":
    solve()