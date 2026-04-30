def solution(sales, links):
    n = len(sales)
    node_list = [[] for _ in range(n)]
    
    for start, end in links:
        node_list[start - 1].append(end - 1)
    
    DP = [[0, 0] for _ in range(n)]
    
    
    def DFS(index):
        if not node_list[index]:
            DP[index][1] = sales[index]
            return
        
        total = 0
        add_cost = float('inf')
        flag = False
        for next_node in node_list[index]:
            DFS(next_node)
            
            total += min(DP[next_node][0], DP[next_node][1])
            add_cost = min(add_cost, DP[next_node][1] - DP[next_node][0])
            
            if DP[next_node][0] >= DP[next_node][1]:
                flag = True
                
        if flag:
            DP[index][0] = total
        else:
            DP[index][0] = total + add_cost
        
        DP[index][1] = total + sales[index]
        return
    
    
    DFS(0)
    return min(DP[0])