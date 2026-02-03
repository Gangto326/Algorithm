import sys, heapq

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    num_list = list(map(int, list(read().rstrip())))

    heap = []
    count = K
    for index, num in enumerate(num_list):
        while heap and heap[0][0] < num and count:
            heapq.heappop(heap)
            count -= 1
        
        heapq.heappush(heap, (num, index))

    answer = ""

    if count:
        heap.sort(key = lambda x: (-x[0], -x[1]))

        while count:
            heap.pop()
            count -= 1

    heap.sort(key = lambda x: x[1])

    for num, _ in heap:
        answer += str(num)
    
    print(answer)


if __name__ == "__main__":
    solve()