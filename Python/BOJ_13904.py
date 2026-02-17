import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))

    heap = []
    for _ in range(N):
        day, cost = int(next(iterator)), int(next(iterator))
        heapq.heappush(heap, (-cost, day))

    answer = 0
    check = [True] * 1010
    while heap:
        cost, day = heapq.heappop(heap)
        cost *= -1

        for i in range(day, 0, -1):
            if check[i]:
                check[i] = False
                answer += cost
                break
    
    print(answer)


if __name__ == "__main__":
    solve()