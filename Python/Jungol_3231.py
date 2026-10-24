import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M, H = map(int, read().split())
    board = [[0] * (M + 2)] + [[0] + [H] * M + [0] for _ in range(N)] + [[0] * (M + 2)]
    node_list = [[[] for _ in range(M + 2)] for _ in range(N + 2)]

    for i in range(N + 1):
        for j, k in enumerate(map(int, read().split())):
            if k != -1:
                node_list[i][j + 1].append((i + 1, j + 1, k))
                node_list[i + 1][j + 1].append((i, j + 1, k))

    for i in range(N):
        for j, k in enumerate(map(int, read().split())):
            if k != -1:
                node_list[i + 1][j].append((i + 1, j + 1, k))
                node_list[i + 1][j + 1].append((i + 1, j, k))
    
    dijkstra = []
    for row in range(N + 2):
        for col in range(M + 2):
            if board[row][col] == 0:
                heapq.heappush(dijkstra, (0, row, col))
    
    while dijkstra:
        max_h, r, c = heapq.heappop(dijkstra)

        if board[r][c] < max_h:
            continue

        for nr, nc, h in node_list[r][c]:
            next_h = max(max_h, h)

            if board[nr][nc] > next_h:
                board[nr][nc] = next_h
                heapq.heappush(dijkstra, (next_h, nr, nc))

    answer = 0
    for i in range(1, N + 1):
        answer += sum(board[i])
    
    print(answer)


if __name__ == "__main__":
    solve()