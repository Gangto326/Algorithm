import sys, heapq
from collections import defaultdict

def solve():
    read = sys.stdin.buffer.readline
    N = int(read())
    heap = []

    for i in range(N):
        start, end = map(int, read().split())
        heapq.heappush(heap, (start, 1, i))
        heapq.heappush(heap, (end, -1, i))

    answer_list = [0] * N
    answer = 0
    count = 0
    
    seats = []
    for i in range(1, 100001):
        heapq.heappush(seats, i)
    
    count_dict = defaultdict(int)
    while heap:
        time, cost, index = heapq.heappop(heap)
        count += cost
        answer = max(answer, count)

        if cost == 1:
            answer_list[index] = heapq.heappop(seats)
            count_dict[answer_list[index]] += 1
        
        else:
            heapq.heappush(seats, answer_list[index])

    print(answer)
    print(*count_dict.values())


if __name__ == "__main__":
    solve()