from collections import deque

def solution(storage, requests):
    R, C = len(storage), len(storage[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    board = [['*'] * (C + 2)] + [['*'] + list(s.strip()) + ['*'] for s in storage] + [['*'] * (C + 2)]
    
    alpha_dict = {}
    for row in range(1, R + 1):
        for col in range(1, C + 1):
            if board[row][col] in alpha_dict:
                alpha_dict[board[row][col]].add((row, col))
            
            else:
                alpha_dict[board[row][col]] = {(row, col)}
    
    count = 0
    blank_set = set()
    for request in requests:
        
        BFS = deque()
        for rc in blank_set:
            for i in range(4):
                nr, nc = rc[0] + dx[i], rc[1] + dy[i]
                
                if board[nr][nc] == '*':
                    BFS.append((rc[0], rc[1]))
                    board[rc[0]][rc[1]] = '*'
                    break
            
        while BFS:
            rc = BFS.popleft()
            blank_set.remove(rc)
            
            for i in range(4):
                nr, nc = rc[0] + dx[i], rc[1] + dy[i]
                
                if board[nr][nc] == '-':
                    BFS.append((nr, nc))
                    board[nr][nc] = '*'
                    break
        
        if len(request) == 1:
            if not request in alpha_dict:
                continue
            
            check = set()
            for rc in alpha_dict[request]:
                for i in range(4):
                    nr, nc = rc[0] + dx[i], rc[1] + dy[i]
                    
                    if board[nr][nc] == '*':
                        count += 1
                        check.add(rc)
                        break
            
            for rc in check:
                board[rc[0]][rc[1]] = '*'
                alpha_dict[request].remove(rc)
                
        else:
            request = request[0]
            if not request in alpha_dict:
                continue
            
            count += len(alpha_dict[request])
            for rc in alpha_dict[request]:
                flag = False
                
                for i in range(4):
                    nr, nc = rc[0] + dx[i], rc[1] + dy[i]
                    
                    if board[nr][nc] == '*':
                        board[rc[0]][rc[1]] = '*'
                        flag = True
                        break
                
                if not flag:
                    board[rc[0]][rc[1]] = '-'
                    blank_set.add(rc)
            
            alpha_dict.pop(request)
    
    answer = R * C - count
    return answer