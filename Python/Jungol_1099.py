import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())

    heap = []
    for _ in range(N):
        start, end = read().split()
        
        y, m, d = map(int, start.split('.'))
        heapq.heappush(heap, y * 100000 + m * 1000 + d * 10 + 1)

        y, m, d = map(int, end.split('.'))
        heapq.heappush(heap, y * 100000 + m * 1000 + d * 10)

    answer = 0
    total = 0
    while heap:
        num = heapq.heappop(heap)

        if num % 10 == 1:
            total += 1
        else:
            total -= 1

        answer = max(answer, total)

    print(answer)


if __name__ == '__main__':
    solve()