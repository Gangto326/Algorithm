import heapq

def solution(jobs):
    N = len(jobs)
    index = 0
    answer = 0
    heap = []
    jobs.sort(key = lambda x: x[0])
    
    time = 0
    while True:
        if not heap:
            if index >= N:
                break
                
            start_time = float('inf')
            
            for i in range(index, N):
                if jobs[i][0] <= start_time:
                    job = jobs[i]
                    heapq.heappush(heap, (job[1], job[0], i))
                    index = i
                    start_time = jobs[i][0]
            
            index += 1
            if time < start_time:
                time = start_time
            
        r, s, i = heapq.heappop(heap)
        time += r
        answer += (time - s)
        
        while index < N and jobs[index][0] <= time:
            job = jobs[index]
            heapq.heappush(heap, (job[1], job[0], index))
            index += 1
        
    
    return answer // N