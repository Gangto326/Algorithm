import sys, heapq

read = sys.stdin.readline
N = int(read().rstrip())
building_list = []

for _ in range(N):
    L, H, R = map(int, read().split())
    building_list.append((L, -H, R))
    building_list.append((R, 0, 0))

building_list.sort()

queue = [(0, float('inf'))]
height = 0
answer = []
for s, h, e in building_list:
    if h != 0:
        heapq.heappush(queue, (h, e))
    
    else:
        while queue and queue[0][1] <= s:
            heapq.heappop(queue)
    
    next_height = -queue[0][0]
    if height != next_height:
        height = next_height
        answer.extend((s, height))

print(*answer)