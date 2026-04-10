import sys, heapq

def solve():
    read = sys.stdin.buffer.readline
    N, M = map(int, read().split())
    num_list = [tuple(map(int, read().split())) for _ in range(N)]
    num_list.sort(key = lambda x: x[0])
    mask_list = [tuple(map(int, read().split())) for _ in range(M)]
    mask_list.sort(key = lambda x: x[0])

    heap = []
    answer = 0
    index = 0

    for cost, count in mask_list:
        while index < N and num_list[index][0] <= cost:
            heapq.heappush(heap, num_list[index][1])
            index += 1

        while count and heap:
            if heap[0] >= cost:
                count -= 1
                answer += 1
            
            heapq.heappop(heap)
    
    print(answer)


if __name__ == "__main__":
    solve()