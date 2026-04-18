def solution(n, q, ans):
    comb_list = []
    
    def DFS(num, count, li):
        nonlocal n
        
        if count == 5:
            comb_list.append(tuple(li))
            return
        
        for i in range(num, n + 1):
            li.append(i)
            DFS(i + 1, count + 1, li)
            li.pop()
    
    
    DFS(1, 0, [])
    N = len(q)
    answer = 0
    
    
    def solve(index, comb):
        nonlocal N, answer
        
        if index >= N:
            answer += 1
            return
        
        count = 0
        for num in q[index]:
            if num in comb:
                count += 1
        
        if ans[index] == count:
            solve(index + 1, comb)
        
    
    for comb in comb_list:
        solve(0, set(comb))
    
    return answer