def solution(players, m, k):
    server = [0] * 24
    
    answer = 0
    for i in range(24):
        if players[i] >= (server[i] + 1) * m:
            add_server = (players[i] // m) - server[i]
            
            for j in range(k):
                if i + j < 24:
                    server[i + j] += add_server
            
            answer += add_server
    
    return answer