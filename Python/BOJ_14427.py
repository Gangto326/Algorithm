import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    heap = []
    version = [0] * (N + 1)

    for i in range(1, N + 1):
        heapq.heappush(heap, (int(next(iterator)), i, 0))

    query_num = int(next(iterator))
    for _ in range(query_num):
        query = int(next(iterator))

        if query == 2:
            while heap[0][-1] != version[heap[0][1]]:
                heapq.heappop(heap)
            
            print(heap[0][1])
        
        else:
            index, value = int(next(iterator)), int(next(iterator))
            version[index] += 1
            heapq.heappush(heap, (value, index, version[index]))


if __name__ == "__main__":
    solve()