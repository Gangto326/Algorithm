import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    node_list = [[] for _ in range(N)]

    for i in range(1, N):
        node_list[num_list[i]].append(i)
    

    def DFS(index):
        if not node_list[index]:
            return 1
        
        count_heap = []
        next_count_heap = []
        for next_node in node_list[index]:
            heapq.heappush(count_heap, DFS(next_node))
        
        count = len(node_list[index])
        while count:
            heapq.heappush(next_count_heap, heapq.heappop(count_heap) + count)
            count -= 1
        
        min_cost = 0
        while next_count_heap:
            min_cost = heapq.heappop(next_count_heap)
        
        return min_cost


    print(DFS(0) - 1)


if __name__ == "__main__":
    solve()