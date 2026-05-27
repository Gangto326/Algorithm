def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start_time = 3600 * h1 + 60 * m1 + s1
    end_time = 3600 * h2 + 60 * m2 + s2
    
    if start_time == 0 or start_time == 12 * 3600:
        answer += 1
    
    while start_time < end_time:
        h = start_time / 120 % 360
        m = start_time / 10 % 360
        s = start_time * 6 % 360
        
        start_time += 1
        
        nh = start_time / 120 % 360 if start_time / 120 % 360 != 0 else 360
        nm = start_time / 10 % 360 if start_time / 10 % 360 != 0 else 360
        ns = start_time * 6 % 360 if start_time * 6 % 360 != 0 else 360
        
        if h > s and nh <= ns:
            answer += 1
        if m > s and nm <= ns:
            answer += 1
        if ns == nm == nh:
            answer -= 1
    
    return answer