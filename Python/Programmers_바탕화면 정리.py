def solution(wallpaper):
    N = len(wallpaper)
    M = len(wallpaper[0])
    answer = [float('inf'), float('inf'), 0, 0]
    
    for row in range(N):
        for col in range(M):
            if wallpaper[row][col] == '#':
                if row < answer[0]:
                    answer[0] = row
                
                if col < answer[1]:
                    answer[1] = col
                
                if row + 1 > answer[2]:
                    answer[2] = row + 1
                
                if col + 1 > answer[3]:
                    answer[3] = col + 1
    
    return answer