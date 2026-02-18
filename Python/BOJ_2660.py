import sys

def solve():
    MAX_VALUE = 100_000
    read = sys.stdin.readline
    N = int(read())
    DP = [[100_000] * (N+1) for _ in range(N+1)]

    while True:
        a, b = map(int, read().split())

        if a == -1 and b == -1:
            break

        DP[a][b] = 1
        DP[b][a] = 1
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue

                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])
    
    answer = MAX_VALUE
    answer_list = []

    for i in range(1, N+1):
        score = 0

        for j in range(1, N+1):
            if DP[i][j] != MAX_VALUE:
                score = max(score, DP[i][j])
        
        if score < answer:
            answer = score
            answer_list = [i]
        elif score == answer:
            answer_list.append(i)

    print(answer, len(answer_list))
    print(*answer_list)


if __name__ == "__main__":
    solve()