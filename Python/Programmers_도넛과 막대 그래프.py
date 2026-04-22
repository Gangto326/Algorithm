from collections import deque

def solution(edges):
    MAX_VALUE = 1_000_010
    
    node_dict = {}
    indegree = [0] * MAX_VALUE
    
    for start, end in edges:
        if start in node_dict:
            node_dict[start].append(end)
        else:
            node_dict[start] = [end]
        
        indegree[end] += 1
    
    answer = [0, 0, 0, 0]
    for key in node_dict:
        if not indegree[key] and len(node_dict[key]) >= 2:
            answer[0] = key
            break
    
    check = [True] * MAX_VALUE
    check[answer[0]] = False
    
    for graph in node_dict[answer[0]]:
        BFS = deque()
        BFS.append(graph)
        check[graph] = False
        
        if indegree[graph] == 1:
            answer[2] += 1
            continue
        
        if indegree[graph] == 3:
            answer[3] += 1
            continue
            
        if indegree[graph] == 2:
            if not graph in node_dict:
                answer[2] += 1
                continue
        
        flag = False
        while BFS:
            node = BFS.popleft()
            
            if node != graph and indegree[node] == 2:
                answer[3] += 1
                flag = True
                break
                
            if not node in node_dict:
                answer[2] += 1
                flag = True
                break
            
            for next_node in node_dict[node]:
                if check[next_node]:
                    BFS.append(next_node)
                    check[next_node] = False
        
        if not flag:
            answer[1] += 1
            
        
    return answer