def solution(park, routes):
    N = len(park)
    M = len(park[0])
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    way_dict = {"E": 2, "N": 1, "S": 0, "W": 3}
    sr, sc = -1, -1
    
    for row in range(N):
        for col in range(M):
            if park[row][col] == "S":
                sr, sc = row, col
                break
        
        if sr != -1:
            break
    
    for route in routes:
        nr, nc = sr, sc
        way, count = route.split(" ")
        way = way_dict[way]
        count = int(count)
        flag = True
        
        for i in range(count):
            nr, nc = nr + dy[way], nc + dx[way]
            
            if 0 <= nr < N and 0 <= nc < M:
                if park[nr][nc] == "X":
                    flag = False
                    break
            
            else:
                flag = False
                break
        
        if flag:
            sr, sc = nr, nc
    
    answer = [sr, sc]
    return answer