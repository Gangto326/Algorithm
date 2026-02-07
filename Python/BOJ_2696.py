import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))

    for tc in range(T):
        N = int(next(iterator))
        min_heap = []
        max_heap = []
        answer_list = []

        for i in range(1, N+1):
            num = int(next(iterator))

            if not min_heap:
                heapq.heappush(min_heap, -num)
            
            else:
                if min_heap[0] < -num:
                    heapq.heappush(min_heap, -num)
                else:
                    heapq.heappush(max_heap, num)

            if i % 2:
                while len(min_heap) < len(max_heap):
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
                
                while len(min_heap) != len(max_heap) + 1:
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))

                answer_list.append(-min_heap[0])

        print(len(answer_list))

        for i in range(1, len(answer_list)):
            print(answer_list[i-1], end = " ")

            if i % 10 == 0:
                print("\n", end = "")
        print(answer_list[-1])


if __name__ == "__main__":
    solve()