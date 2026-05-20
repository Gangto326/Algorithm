def solution(board, h, w):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    N = len(board)
    
    answer = 0
    for i in range(4):
        nr, nc = h + dx[i], w + dy[i]
        
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == board[h][w]:
                answer += 1
    
    return answer