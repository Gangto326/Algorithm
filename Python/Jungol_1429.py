import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    indegree = [0] * (N + 1)
    next_node_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = int(next(iterator)), int(next(iterator))
        indegree[B] += 1
        next_node_list[A].append(B)
    
    heap = []
    for i in range(1, N + 1):
        if not indegree[i]:
            heapq.heappush(heap, i)
    
    answer_list = []
    while heap:
        node = heapq.heappop(heap)
        answer_list.append(node)

        for next_node in next_node_list[node]:
            indegree[next_node] -= 1

            if not indegree[next_node]:
                heapq.heappush(heap, next_node)
    
    print(*answer_list)


if __name__ == "__main__":
    solve()