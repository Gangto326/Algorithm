import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    points_list = []

    for _ in range(N):
        start, end = map(int, read().split())
        if start > end:
            start, end = end, start
        
        points_list.append((start, end))
    
    points_list.sort(key = lambda x: x[1])

    length = int(read().rstrip())
    queue = []
    answer = 0
    for start, end in points_list:
        if start >= end - length:
            heapq.heappush(queue, start)
        
        while queue:
            if queue[0] < end - length:
                heapq.heappop(queue)
            else:
                break
        
        answer = max(answer, len(queue))
    
    print(answer)
    

if __name__ == "__main__":
    solve()