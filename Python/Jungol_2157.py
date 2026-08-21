import sys, heapq

def solve():
    read = sys.stdin.readline
    N, C, F = map(int, read().split())

    num_list = []
    for _ in range(C):
        score, cost = map(int, read().split())
        num_list.append((score, cost))

    num_list.sort(key = lambda x: x[0])

    left_heap = []
    left_cost = [float('inf')] * C

    total = 0
    for i in range(N // 2):
        heapq.heappush(left_heap, -num_list[i][1])
        total += num_list[i][1]

    left_cost[N // 2 - 1] = total
    for i in range(N // 2, C):
        if len(left_heap) >= N // 2:
            heapq.heappush(left_heap, -num_list[i][1])
            left_cost[i] = left_cost[i - 1] + heapq.heappop(left_heap) + num_list[i][1]

    right_heap = []
    right_cost = [float('inf')] * C

    total = 0
    for i in range(N // 2):
        heapq.heappush(right_heap, -num_list[C - i - 1][1])
        total += num_list[C - i - 1][1]
    
    right_cost[C - (N // 2)] = total
    for i in range(C - (N // 2) - 1, -1, -1):
        heapq.heappush(right_heap, -num_list[i][1])
        right_cost[i] = right_cost[i + 1] + heapq.heappop(right_heap) + num_list[i][1]

    for i in range(C - (N // 2) - 1, N // 2 - 1, -1):
        if left_cost[i - 1] + right_cost[i + 1] + num_list[i][1] <= F:
            print(num_list[i][0])
            return
        
    print(-1)


if __name__ == "__main__":
    solve()