from collections import deque

def solution(n, edge):
    node_list = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        node_list[a].append(b)
        node_list[b].append(a)
    
    BFS = deque()
    BFS.append((1, 0))
    
    check = [float('inf')] * (n + 1)
    check[1] = 0
    
    max_count = 0
    while BFS:
        node, cost = BFS.popleft()
        
        max_count = max(max_count, cost)
        
        next_cost = cost + 1
        for next_node in node_list[node]:
            if check[next_node] == float('inf'):
                check[next_node] = next_cost
                BFS.append((next_node, next_cost))
    
    answer = 0
    for i in range(1, n + 1):
        if check[i] == max_count:
            answer += 1
            
    return answer