import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    H = int(next(iterator))
    N, Q = int(next(iterator)), int(next(iterator))

    num_list = [int(next(iterator)) for _ in range(N)]
    num_list.sort(reverse = True)

    heap = []

    count = 0
    total = 0
    for num in num_list:
        if total < H:
            total += num
            count += 1
            heapq.heappush(heap, num)
    
    if total < H:
        print(-1)
    else:
        print(count)
    
    for _ in range(Q):
        num = int(next(iterator))

        total += num
        count += 1
        heapq.heappush(heap, num)

        if total < H:
            print(-1)

        else:
            while heap:
                if total - heap[0] >= H:
                    total -= heapq.heappop(heap)
                    count -= 1
                else:
                    break

            print(count)


if __name__ == "__main__":
    solve()