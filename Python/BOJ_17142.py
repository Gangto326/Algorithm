import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [[1] * (N + 2)] + [[1] + list(map(int, read().split())) + [1] for _ in range(N)] + [[1] * (N + 2)]
    virus_list = []
    comb_list = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    total_count = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 2:
                virus_list.append((i, j))
                
            elif board[i][j] == 0:
                total_count += 1

    if not total_count:
        print(0)
        return
    

    def DFS(index, comb, virus_count, total):
        if len(comb) == total:
            comb_list.append(comb[:])
            return

        if index >= virus_count:
            return
        
        for i in range(index, virus_count):
            comb.append(virus_list[i])
            DFS(i + 1, comb, virus_count, total)
            comb.pop()


    DFS(0, [], len(virus_list), M)


    def BFS(virus_list, total_count):
        bfs = deque()
        time = 0
        visited = set()
        visited_virus = set()

        for virus in virus_list:
            bfs.append(virus)
            visited_virus.add(virus)
        
        while bfs:
            next_bfs = deque()

            while bfs:
                row, col = bfs.popleft()

                for i in range(4):
                    nr, nc = row + dx[i], col + dy[i]

                    if board[nr][nc] == 2 and not (nr, nc) in visited_virus:
                        next_bfs.append((nr, nc))
                        visited_virus.add((nr, nc))


                    elif board[nr][nc] == 0 and not (nr, nc) in visited:
                        next_bfs.append((nr, nc))
                        visited.add((nr, nc))
            
            time += 1
            bfs = next_bfs

            if len(visited) == total_count:
                return time
        
        return float('inf')

    answer = float('inf')
    for comb in comb_list:
        answer = min(answer, BFS(comb, total_count))
                
    print(answer if answer != float('inf') else -1)


if __name__ == "__main__":
    solve()