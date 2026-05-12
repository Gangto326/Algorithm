from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    board = [[-1] * 101 for _ in range(101)]
    
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for col in range(x1, x2 + 1):
            for row in range(y1, y2 + 1):
                if x1 < col < x2 and y1 < row < y2:
                    board[row][col] = 0
                elif board[row][col]:
                    board[row][col] = 1
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    BFS = deque()
    BFS.append((characterY, characterX, 0))
    
    check = [[True] * 101 for _ in range(101)]
    check[characterY][characterX] = False
    
    while BFS:
        row, col, count = BFS.popleft()
        
        if row == itemY and col == itemX:
            return count // 2
        
        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]
            
            if nr < 0 or nc < 0 or nr > 100 or nc > 100:
                continue
                
            if board[nr][nc] == 1 and check[nr][nc]:
                BFS.append((nr, nc, count + 1))
                check[nr][nc] = False
    
    return -1