import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    heap = []

    for _ in range(N):
        index, start, end = int(next(iterator)), int(next(iterator)), int(next(iterator))
        heapq.heappush(heap, (start, True))
        heapq.heappush(heap, (end, False))

    answer = 0
    total = 0
    while heap:
        time, flag = heapq.heappop(heap)

        if flag:
            total += 1
            answer = max(answer, total)

        if not flag:
            total -= 1

    print(answer)


if __name__ == "__main__":
    solve()