import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    plus_heap = []
    minus_heap = []
    for _ in range(N):
        num = -int(next(iterator))

        if num < 0:
            heapq.heappush(plus_heap, num)
        else:
            heapq.heappush(minus_heap, -num)

    answer = 0
    while plus_heap:
        if len(plus_heap) >= 2:
            first, sec = -heapq.heappop(plus_heap), -heapq.heappop(plus_heap)

            if first <= 1 or sec <= 1:
                answer += first + sec

            else:
                answer += first * sec
        
        else:
            answer += -heapq.heappop(plus_heap)

    while minus_heap:
        if len(minus_heap) >= 2:
            first, sec = heapq.heappop(minus_heap), heapq.heappop(minus_heap)
            answer += first * sec
        
        else:
            num = heapq.heappop(minus_heap)
            answer += num

    print(answer)


if __name__ == "__main__":
    solve()