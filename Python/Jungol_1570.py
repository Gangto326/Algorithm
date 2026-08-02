import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    answer_list = []
    min_heap = []
    max_heap = []

    num = int(next(iterator))
    answer_list.append(num)
    heapq.heappush(min_heap, -num)

    for _ in range(N // 2):
        for i in range(2):
            num = int(next(iterator))

            if -num > min_heap[0]:
                heapq.heappush(min_heap, -num)
            else:
                heapq.heappush(max_heap, num)
        
        while len(min_heap) != len(max_heap) + 1:
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            else:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        answer_list.append(-min_heap[0])
    
    print("\n".join(map(str, answer_list)))


if __name__ == "__main__":
    solve()