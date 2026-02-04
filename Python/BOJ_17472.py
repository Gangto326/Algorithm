import sys, heapq
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [list(map(int, read().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    stamp = 2
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                board[row][col] = stamp

                BFS = deque()
                BFS.append((row, col))

                while BFS:
                    r, c = BFS.popleft()

                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]

                        if nr < 0 or nc < 0 or nr >= N or nc >= M:
                            continue
                        
                        if board[nr][nc] == 1:
                            board[nr][nc] = stamp
                            BFS.append((nr, nc))

                stamp += 1

    heap = []
    for row in range(N):
        for col in range(M):
            if board[row][col]:
                start_land = board[row][col]

                for i in range(4):
                    length = 0

                    nr, nc = row, col
                    while True:
                        nr += dx[i]
                        nc += dy[i]

                        if nr < 0 or nc < 0 or nr >= N or nc >= M:
                            break

                        if board[nr][nc] == start_land:
                            break
                        
                        if board[nr][nc] and board[nr][nc] != start_land:
                            if length >= 2:
                                heapq.heappush(heap, (length, start_land, board[nr][nc]))
                            break
                        
                        length += 1


    def find(index):
        if parents[index] == index:
            return index

        parents[index] = find(parents[index])
        return parents[index]
    

    def union(a, b):
        pa = find(a)
        pb = find(b)

        if pa == pb:
            return False

        parents[pa] = b
        return True


    parents = [i for i in range(stamp+1)]
    land_count = stamp - 3
    answer = 0

    while heap and land_count:
        cost, a, b = heapq.heappop(heap)

        if union(a, b):
            answer += cost
            land_count -= 1
    
    print(answer if not land_count else -1)


if __name__ == "__main__":
    solve()