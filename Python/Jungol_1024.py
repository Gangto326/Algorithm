import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    board = [list(map(int, read().split())) for _ in range(N)]

    DP = [[0] * M for _ in range(N)]
    DP[0][0] = 1

    heap = []
    for row in range(N):
        for col in range(M):
            heapq.heappush(heap, (-board[row][col], row, col))

    while heap:
        cost, row, col = heapq.heappop(heap)

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] > -cost:
                    DP[row][col] += DP[nr][nc]
    
    print(DP[-1][-1])


if __name__ == "__main__":
    solve()