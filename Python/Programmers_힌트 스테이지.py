def solution(cost, hint):
    n = len(cost)
    answer = float('inf')
    
    
    def DFS(index, hint_list, total):
        nonlocal n, answer
        
        if index >= n - 1:
            answer = min(answer, total + cost[index][min(n - 1, hint_list[index+ 1])])
            return
        
        next_total = total
        next_total += cost[index][min(n - 1, hint_list[index+ 1])]
        
        DFS(index + 1, hint_list, next_total)
        
        next_total += hint[index][0]
        for i in hint[index][1:]:
            hint_list[i] += 1
        
        DFS(index + 1, hint_list, next_total)
        
        for i in hint[index][1:]:
            hint_list[i] -= 1
    
    
    DFS(0, [0] * (n + 1), 0)
    
    return answer