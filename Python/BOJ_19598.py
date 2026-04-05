import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    heap = []

    for _ in range(N):
        start, end = map(int, read().split())

        heapq.heappush(heap, (start, 1))
        heapq.heappush(heap, (end, -1))

    answer = 0
    total = 0
    while heap:
        _, count = heapq.heappop(heap)

        total += count
        answer = max(answer, total)
    
    print(answer)


if __name__ == "__main__":
    solve()