def solution(cookie):
    N = len(cookie)
    answer = 0
    
    for i in range(N - 1):
        left = i
        left_total = cookie[left]
        
        right = i + 1
        right_total = cookie[right]
        
        while True:
            if left_total > right_total:
                right += 1
                
                if right >= N:
                    break
                    
                right_total += cookie[right]
                
            else:
                if left_total == right_total:
                    answer = max(answer, left_total)
                    
                left -= 1
                
                if left < 0:
                    break
                
                left_total += cookie[left]
    
    return answer