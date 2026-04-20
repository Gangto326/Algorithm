def solution(n, infection, edges, k):
    permutation_list = []
    type_list = [1, 2, 3]
    
    
    def make_perm(li):
        nonlocal k
        
        if len(li) == k:
            permutation_list.append(tuple(li))
            return
        
        for t in type_list:
            li.append(t)
            make_perm(li)
            li.pop()
    
    
    make_perm([])
    
    node_list = [[[] for _ in range(4)] for _ in range(n + 1)]
    for a, b, t in edges:
        node_list[a][t].append((b))
        node_list[b][t].append((a))
    
    
    def solve(perm):
        nonlocal infection, n, k
        
        start_node = [infection]
        check = [False] * (n + 1)
        check[infection] = True
        
        count = 1
        for i in range(k):
            t = perm[i]
            stack = []
            
            for j in range(1, n + 1):
                if check[j]:
                    for next_node in node_list[j][t]:
                        if not check[next_node]:
                            check[next_node] = True
                            count += 1
                            stack.append(next_node)
                
            while stack:
                node = stack.pop()
                
                for next_node in node_list[node][t]:
                    if not check[next_node]:
                        check[next_node] = True
                        count += 1
                        stack.append(next_node)
                
        return count
        
        
    answer = 0
    for perm in permutation_list:
        answer = max(answer, solve(perm))
        
    return answer