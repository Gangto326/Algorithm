import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [list(map(int, read().split())) for _ in range(N)]

    ALL_VISITED = 1 << N
    DP = [float('inf')] * ALL_VISITED
    DP[0] = 0
    
    for visited in range(ALL_VISITED):
        if DP[visited] == float('inf'):
            continue

        index = bin(visited).count('1')

        for i in range(N):
            if not visited & (1 << i):
                next_visited = visited ^ (1 << i)
                DP[next_visited] = min(DP[next_visited], DP[visited] + board[index][i])
        
    print(DP[-1])
                

if __name__ == "__main__":
    solve()