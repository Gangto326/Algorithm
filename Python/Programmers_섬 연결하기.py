import heapq

def solution(n, costs):
    heap = []
    
    for a, b, cost in costs:
        heapq.heappush(heap, (cost, a, b))
    
    parents = [i for i in range(n + 1)]
    
    
    def find(index):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]
    
    
    def union(a, b):
        ap = find(a)
        bp = find(b)
        
        if ap == bp:
            return False
        
        parents[ap] = bp
        return True
    
    count = 1
    answer = 0
    while heap:
        cost, a, b = heapq.heappop(heap)
        
        if union(a, b):
            count += 1
            answer += cost
        
        if count == n:
            break
    
    return answer