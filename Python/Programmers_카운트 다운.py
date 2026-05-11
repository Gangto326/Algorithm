def solution(target):
    DP = [[float('inf'), float('inf')] for _ in range(target + 1)]
    DP[0] = [0, 0]
    
    for i in range(target + 1):
        for dart in range(1, 21):
            if i + dart > target:
                continue
            
            if DP[i + dart][0] > DP[i][0] + 1:
                DP[i + dart] = [DP[i][0] + 1, DP[i][1] + 1]
            
            elif DP[i + dart][0] == DP[i][0] + 1:
                DP[i + dart] = [DP[i][0] + 1, max(DP[i][1] + 1, DP[i + dart][1])]
            
            
            for times in range(2, 4):
                darts = dart * times
                
                if i + darts > target:
                    break
                
                if DP[i + darts][0] > DP[i][0] + 1:
                    DP[i + darts] = [DP[i][0] + 1, DP[i][1]]
                
                elif DP[i + darts][0] == DP[i][0] + 1:
                    DP[i + darts] = [DP[i][0] + 1, max(DP[i][1], DP[i + darts][1])]
                
        if i + 50 <= target:
            if DP[i + 50][0] > DP[i][0] + 1:
                DP[i + 50] = [DP[i][0] + 1, DP[i][1] + 1]
            
            elif DP[i + 50][0] == DP[i][0] + 1:
                DP[i + 50] = [DP[i][0] + 1, max(DP[i][1] + 1, DP[i + 50][1])]
    
    return DP[-1]