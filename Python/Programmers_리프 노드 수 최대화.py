def solution(dist_limit, split_limit):
    answer = 0
    
    two_count = 0
    while (2 ** two_count) <= split_limit:
        three_count = 0
        
        while (2 ** two_count) * (3 ** three_count) <= split_limit:
            count = 1
            dists = dist_limit
            cap = 1
            
            for _ in range(two_count):
                if dists == 0:
                    break
                    
                use = min(cap, dists)
                count += use * 1
                cap = use * 2
                dists -= use
            
            for _ in range(three_count):
                if dists == 0:
                    break
                    
                use = min(cap, dists)
                count += use * 2
                cap = use * 3
                dists -= use
            
            answer = max(answer, count)
            three_count += 1
            
        two_count += 1
        
    return answer