import heapq

def solution(targets):
    heap = []
    for s, e in targets:
        heapq.heappush(heap, (e, s))
    
    answer = 0
    shoot = 0
    while heap:
        e, s = heapq.heappop(heap)
        
        if s >= shoot:
            shoot = e
            answer += 1
    
    return answer