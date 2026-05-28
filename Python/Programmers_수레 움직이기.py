from collections import deque

def solution(maze):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    N, M = len(maze), len(maze[0])
    
    r_row, r_col = 0, 0
    b_row, b_col = 0, 0
    
    rg_row, rg_col = 0, 0
    bg_row, bg_col = 0, 0
    
    for row in range(N):
        for col in range(M):
            if maze[row][col] == 1:
                r_row, r_col = row, col
            elif maze[row][col] == 2:
                b_row, b_col = row, col
            elif maze[row][col] == 3:
                rg_row, rg_col = row, col
            elif maze[row][col] == 4:
                bg_row, bg_col = row, col
    
    BFS = deque()
    
    # 빨강 좌표, 파랑 좌표, 빨강 체크(2진수), 파랑 체크(2진수), 카운트
    BFS.append([(r_row, r_col), (b_row, b_col), (1 << (r_row*4 + r_col)), (1 << (b_row*4 + b_col)), 0])
    answer = 0
    
    while BFS:
        R, B, RC, BC, count = BFS.popleft()
        rr, rc = R
        br, bc = B
        
        if rr == rg_row and rc == rg_col and br == bg_row and bc == bg_col:
            answer = count
            break
        
        for i in range(4):
            nrr, nrc = rr + dx[i], rc + dy[i]
            
            if rr == rg_row and rc == rg_col:
                nrr = rr
                nrc = rc
            
            elif nrr < 0 or nrc < 0 or nrr >= N or nrc >= M:
                continue
            
            elif maze[nrr][nrc] == 5:
                continue
            
            elif (RC & (1 << (nrr*4 + nrc))):
                continue
                
            for j in range(4):
                nbr, nbc = br + dx[j], bc + dy[j]
                
                if br == bg_row and bc == bg_col:
                    if not (nrr == br and nrc == bc):
                        BFS.append([(nrr, nrc), (br, bc), RC | (1 << (nrr*4 + nrc)), BC, count + 1])
                        break
                    
                if nbr < 0 or nbc < 0 or nbr >= N or nbc >= M:
                    continue
                
                if maze[nbr][nbc] == 5:
                    continue
                    
                if (nbr == nrr and nbc == nrc) or (BC & (1 << (nbr*4 + nbc))):
                    continue
                
                if (nrr == br and nrc == bc) and (nbr == rr and nbc == rc):
                    continue

                BFS.append([(nrr, nrc), (nbr, nbc), RC | (1 << (nrr*4 + nrc)), BC | (1 << (nbr*4 + nbc)), count + 1])
    
    return answer