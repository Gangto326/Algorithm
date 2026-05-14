import sys
sys.setrecursionlimit(300_000)

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    N = len(a)
    
    node_list = [[] for _ in range(N)]
    for u, v in edges:
        node_list[u].append(v)
        node_list[v].append(u)
        
    check = [False] * N
    answer = 0
    
    
    def dfs(node):
        nonlocal answer
        check[node] = True
        
        for next_node in node_list[node]:
            if not check[next_node]:
                total = dfs(next_node)
                a[node] += total
                answer += abs(total)
                
        return a[node]
    
    
    dfs(0)
    return answer