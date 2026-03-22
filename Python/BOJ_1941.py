import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    board = [list(read().strip()) for _ in range(5)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    answer = 0
    selected = []


    def is_connect():
        start = selected[0]
        queue = deque([start])
        visited = set([start])
        comb_set = set(selected)
        
        count = 1
        while queue:
            r, c = queue.popleft()
            
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                
                if (nr, nc) in comb_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    count += 1
                    
        return count == 7


    def DFS(row, col, s_count, y_count):
        nonlocal answer

        if y_count >= 4:
            return
        
        if len(selected) == 7:
            if is_connect():
                answer += 1
            return
        
        for r in range(row, 5):
            start_c = col if r == row else 0

            for c in range(start_c, 5):
                selected.append((r, c))

                if board[r][c] == 'S':
                    DFS(r, c + 1, s_count + 1, y_count)
                else:
                    DFS(r, c + 1, s_count, y_count + 1)
                    
                selected.pop()


    DFS(0, 0, 0, 0)
    print(answer)


if __name__ == "__main__":
    solve()