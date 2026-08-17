import sys

def solve():
    read = sys.stdin.readline
    tc = int(read())

    for _ in range(tc):
        N, M, B = map(int, read().split())
        board = [[float('inf')] * (N + 1) for _ in range(N + 1)]

        for _ in range(M):
            S, E, T = map(int, read().split())
            board[S][E] = min(board[S][E], T)
            board[E][S] = min(board[E][S], T)
        
        for _ in range(B):
            S, E, T = map(int, read().split())
            board[S][E] = min(board[S][E], -T)

        edge_list = []
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if board[i][j] != float('inf'):
                    edge_list.append((i, j, board[i][j]))

        dist = [float('inf')] * (N + 1)
        dist[1] = 0

        for _ in range(N - 1):
            for start, end, cost in edge_list:
                if dist[end] > dist[start] + cost:
                    dist[end] = dist[start] + cost

        flag = False
        for start, end, cost in edge_list:
            if dist[end] > dist[start] + cost:
                flag = True
                break

        if flag:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()