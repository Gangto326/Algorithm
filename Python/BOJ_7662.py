import sys, heapq
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    T = int(read().rstrip())

    for tc in range(T):
        num_dict = defaultdict(int)
        min_heap = []
        max_heap = []

        query_num = int(read().rstrip())
        for _ in range(query_num):
            query, num = read().split()
            num = int(num)

            if query == 'I':
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
                num_dict[num] += 1
            
            elif query == 'D':
                if num > 0:
                    while max_heap:
                        max_num = -heapq.heappop(max_heap)

                        if num_dict[max_num] > 0:
                            num_dict[max_num] -= 1
                            break

                else:
                    while min_heap:
                        min_num = heapq.heappop(min_heap)

                        if num_dict[min_num] > 0:
                            num_dict[min_num] -= 1
                            break
        
        max_answer, min_answer = -float('inf'), float('inf')

        for key, value in num_dict.items():
            if value:
                max_answer = max(max_answer, key)
                min_answer = min(min_answer, key)
        
        if min_answer == float('inf'):
            print("EMPTY")
        else:
            print(max_answer, min_answer)


if __name__ == "__main__":
    solve()