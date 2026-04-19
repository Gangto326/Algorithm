from collections import deque

def solution(land):
    N, M = len(land), len(land[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    check = [[0] * M for _ in range(N)]
    land_num = 0
    land_dict = {}
    
    for row in range(N):
        for col in range(M):
            if check[row][col] == 0 and land[row][col] == 1:
                BFS = deque()
                BFS.append((row, col))
                land_num += 1
                count = 1
                
                check[row][col] = land_num
                while BFS:
                    r, c = BFS.popleft()
                    
                    for i in range(4):
                        nr, nc = r + dx[i], c + dy[i]
                        
                        if 0 <= nr < N and 0 <= nc < M:
                            if land[nr][nc] and not check[nr][nc]:
                                count += 1
                                check[nr][nc] = land_num
                                BFS.append((nr, nc))
                
                land_dict[land_num] = count
    
    answer = 0
    for col in range(M):  
        get_land = set()
        
        for row in range(N):
            if check[row][col]:
                get_land.add(check[row][col])
        
        total = 0
        for i in get_land:
            total += land_dict[i]
        
        answer = max(answer, total)
    
    return answer