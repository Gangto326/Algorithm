import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [list(map(int, read().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    heap = []
    for row in range(N):
        for col in range(N):
            heapq.heappush(heap, (board[row][col], row, col))
    
    DP = [[0] * N for _ in range(N)]
    while heap:
        cost, row, col = heapq.heappop(heap)

        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            
            if board[nr][nc] >= cost:
                continue

            DP[row][col] = max(DP[row][col], DP[nr][nc] + 1)
        
        if not DP[row][col]:
            DP[row][col] = 1

    answer = 0
    for i in range(N):
        answer = max(answer, max(DP[i]))
    
    print(answer)
    

if __name__ == "__main__":
    solve()