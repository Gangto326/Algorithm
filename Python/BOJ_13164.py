import sys, heapq

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    num_list = list(map(int, read().split()))
    heap = []

    for i in range(N - 1):
        heapq.heappush(heap, -(num_list[i + 1] - num_list[i]))
    
    K -= 1
    while K:
        heapq.heappop(heap)
        K -= 1

    answer = 0
    while heap:
        answer -= heapq.heappop(heap)

    print(answer)


if __name__ == "__main__":
    solve()