def solution(tickets):
    N = len(tickets)
    tickets.sort()
    check = [True] * N
    answer = []
    
    
    def DFS(root):
        nonlocal N, answer
        
        if len(root) == (N + 1):
            answer = root[:]
            return
        
        if answer:
            return
        
        for i in range(N):
            if check[i] and tickets[i][0] == root[-1]:
                check[i] = False
                root.append(tickets[i][1])
                
                DFS(root)
                
                check[i] = True
                root.pop()
        
    
    DFS(["ICN"])
    return answer