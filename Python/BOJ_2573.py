import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [list(map(int, read().split())) for _ in range(N)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    seas = set()
    land = set()

    for row in range(N):
        for col in range(M):
            if board[row][col]:
                land.add((row, col))
            else:
                seas.add((row, col))
    

    def BFS():
        nonlocal N, M
        total = len(land)

        if total == 0:
            return False
        
        start = land.pop()
        queue = deque()

        check = set()
        queue.append(start)
        check.add(start)
        land.add(start)

        while queue:
            row, col = queue.popleft()

            for i in range(4):
                nr, nc = row+dx[i], col+dy[i]

                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue
                
                if (nr, nc) in land and not (nr, nc) in check:
                    check.add((nr, nc))
                    queue.appendleft((nr, nc))
        
        if len(check) == total:
            return True

        return False


    answer = 0
    while land:
        answer += 1
        next_seas = set()

        for row, col in land:
            for i in range(4):
                nr, nc = row+dx[i], col+dy[i]

                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue

                if (nr, nc) in seas:
                    board[row][col] -= 1

            if board[row][col] <= 0:
                next_seas.add((row, col))

        for sea in next_seas:
            seas.add(sea)
            land.remove(sea)

        if next_seas:
            if not BFS():
                break
    
    print(answer if land else 0)

if __name__ == "__main__":
    solve()