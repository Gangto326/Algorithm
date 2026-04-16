def solution(gems):
    N = len(gems)
    gem_dict = {}
    
    max_total = 0
    min_range = float('inf')
    answer = [0, 0]
    
    left = 0
    right = -1
    while right < (N - 1):
        right += 1
        
        if gems[right] in gem_dict:
            gem_dict[gems[right]] += 1
            
            while left < right:
                if gem_dict[gems[left]] > 1:
                    gem_dict[gems[left]] -= 1
                    left += 1
                else:
                    if min_range > (right - left):
                        min_range = (right - left)
                        answer[0] = left + 1
                        answer[1] = right + 1
                    break
        
        else:
            gem_dict[gems[right]] = 1
            
            if len(gem_dict) > max_total:
                max_total = len(gem_dict)
                min_range = (right - left)
                answer[0] = left + 1
                answer[1] = right + 1
        
    return answer