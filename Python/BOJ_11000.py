import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    heap = []

    for _ in range(N):
        heapq.heappush(heap, (int(next(iterator)), 'start'))
        heapq.heappush(heap, (int(next(iterator)), 'end'))

    answer = 0
    count = 0
    while heap:
        num, query = heapq.heappop(heap)

        if query == 'start':
            count += 1
        else:
            count -= 1

        answer = max(answer, count)
    
    print(answer)


if __name__ == "__main__":
    solve()