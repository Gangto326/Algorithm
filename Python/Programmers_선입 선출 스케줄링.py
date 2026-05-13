def solution(n, cores):
    if len(cores) >= n:
        return n
    
    n -= len(cores)
    
    left = 1
    right = 10000 * n
    target = 0
    while left <= right:
        mid = (left + right) // 2
        sum_num = sum(mid // i for i in cores)
        
        if sum_num >= n:
            target = mid
            right = mid - 1
        else:
            left = mid + 1
    
    end = sum((target - 1) // i for i in cores)
    n -= end
    
    for index, i in enumerate(cores):
        if target % i == 0:
            n -= 1
            if n == 0:
                return index + 1