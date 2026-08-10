import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    if N == 1:
        print(int(next(iterator)))
        return

    heap = []
    for _ in range(N):
        heapq.heappush(heap, int(next(iterator)))
    
    answer = 0
    while len(heap) != 1:
        first, sec = heapq.heappop(heap), heapq.heappop(heap)
        num = first + sec

        answer += num
        heapq.heappush(heap, num)
    
    print(answer)


if __name__ == "__main__":
    solve()