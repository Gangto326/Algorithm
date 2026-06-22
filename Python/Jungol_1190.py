import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))

    answer = 0
    heap = []
    for num in num_list:
        heapq.heappush(heap, num)
    
    while len(heap) != 1:
        num = heapq.heappop(heap) + heapq.heappop(heap)
        answer += num
        heapq.heappush(heap, num)

    print(answer)
    

if __name__ == "__main__":
    solve()