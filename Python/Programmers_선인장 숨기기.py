from collections import deque

def solution(m, n, h, w, drops):
    board = [[float('inf')] * n for _ in range(m)]
    N = len(drops)
    
    for i in range(N):
        num = i + 1
        row, col = drops[i]
        
        if board[row][col] > num:
            board[row][col] = num
            
    next_board = [[float('inf')] * n for _ in range(m)]
    for row in range(m):
        deq = deque()
        
        for col in range(n):
            if deq and deq[0] < col - w + 1:
                deq.popleft()
            
            while deq and board[row][deq[-1]] >= board[row][col]:
                deq.pop()
            
            deq.append(col)
            next_board[row][col] = board[row][deq[0]]
    
    for i in range(m):
        board[i] = next_board[i][:]
    
    for col in range(n):
        deq = deque()
        
        for row in range(m):
            if deq and deq[0] < row - h + 1:
                deq.popleft()
            
            while deq and board[deq[-1]][col] >= board[row][col]:
                deq.pop()
                
            deq.append(row)
            next_board[row][col] = board[deq[0]][col]
    
    answer = [0, 0]
    max_num = 0
    for row in range(h - 1, m):
        if max_num == float('inf'):
            break
                
        for col in range(w - 1, n):
            if max_num == float('inf'):
                break
                
            if next_board[row][col] > max_num:
                max_num = next_board[row][col]
                answer = [row - (h - 1), col - (w - 1)]
    
    return answer