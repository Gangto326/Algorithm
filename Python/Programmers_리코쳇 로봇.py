from collections import deque

def solution(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    BFS = deque()
    check = [[True] * len(board[0]) for _ in range(len(board))]
    end_x, end_y = 0, 0
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "R":
                check[row][col] = False
                BFS.append((row, col, 0))
                
            elif board[row][col] == "G":
                end_x, end_y = row, col
    
    while BFS:
        row, col, count = BFS.popleft()
        
        if row == end_x and col == end_y:
            return count
        
        for i in range(4):
            nr, nc = row + dx[i], col + dy[i]
            
            while 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if board[nr][nc] == "D":
                    break
                
                nr += dx[i]
                nc += dy[i]
            
            nr -= dx[i]
            nc -= dy[i]
            
            if check[nr][nc]:
                check[nr][nc] = False
                BFS.append((nr, nc, count + 1))
    
    return -1