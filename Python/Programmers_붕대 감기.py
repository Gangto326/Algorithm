def solution(bandage, health, attacks):
    t, x, y = bandage
    time = 0
    max_health = health
    answer = health
    
    for a_time, power in attacks:
        answer += x * (a_time - time - 1)
        answer += y * ((a_time - time - 1) // t)
        
        if answer > max_health:
            answer = max_health
            
        answer -= power
        
        if answer <= 0:
            break
        
        time = a_time
    
    return answer if answer > 0 else -1