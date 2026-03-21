import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    start, end = 301, 1130

    heap = []
    end_list = [0] * (N + 1)

    for i in range(N):
        start_h, start_m, end_h, end_m = map(int, read().split())

        heapq.heappush(heap, (start_h * 100 + start_m, i))
        end_list[i] = end_h * 100 + end_m

    count = 0
    while heap:
        next_start = 0

        while heap:
            if heap[0][0] <= start:
                start_time, index = heapq.heappop(heap)
                next_start = max(next_start, end_list[index])
            else:
                break
        
        count += 1
        if not next_start:
            print(0)
            return

        if next_start > end:
            print(count)
            return
        
        start = next_start

    print(0)


if __name__ == "__main__":
    solve()