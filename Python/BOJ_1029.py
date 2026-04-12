import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [list(map(int, list(read().strip()))) for _ in range(N)]

    ALL_VISITED = 1 << N
    DP = [[float('inf')] * ALL_VISITED for _ in range(N)]
    DP[0][1] = 0

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

                if not visited & (1 << j):
                    continue

                if DP[j][prev_visited] == float('inf'):
                    continue
                
                if DP[j][prev_visited] <= board[j][i]:
                    DP[i][visited] = min(DP[i][visited], board[j][i])
                
    answer = 0
    for visited in range(1, ALL_VISITED):
        for i in range(N):
            if DP[i][visited] != float('inf'):
                answer = max(answer, bin(visited).count('1'))
    
    print(answer)


if __name__ == "__main__":
    solve()