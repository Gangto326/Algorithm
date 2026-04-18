def solution(diffs, times, limit):
    num = len(times)
    left = 1
    right = max(diffs)
    
    while left < right:
        mid = (left + right) // 2
        
        total = 0
        flag = True
        for i in range(num):
            if diffs[i] <= mid:
                total += times[i]
            else:
                total += (times[i] + times[i - 1]) * (diffs[i] - mid)
                total += times[i]
            
            if total > limit:
                flag = False
                break
        
        if not flag:
            left = mid + 1
        else:
            right = mid
    
    answer = left
    return answer