import sys, heapq
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, P = int(next(iterator)), int(next(iterator))
    node_list = [float('inf')] * (N + 1)

    start_node = 0
    for i in range(1, N+1):
        node_list[i] = int(next(iterator))
    
        if node_list[i] < node_list[start_node]:
            start_node = i

    heap = []
    for _ in range(P):
        S, E, length = int(next(iterator)), int(next(iterator)), int(next(iterator))
        heapq.heappush(heap, (2 * length + node_list[S] + node_list[E], S, E))

    parents = [i for i in range(N + 1)]


    def find(node):
        if node == parents[node]:
            return node
        
        parents[node] = find(parents[node])
        return parents[node]
    

    def union(a, b):
        pa = find(a)
        pb = find(b)

        if pa == pb:
            return False
        
        parents[pa] = pb
        return True


    count = 0
    answer = node_list[start_node]
    while heap:
        cost, S, E = heapq.heappop(heap)

        if union(S, E):
            count += 1
            answer += cost

        if count == N - 1:
            print(answer)
            break


if __name__ == "__main__":
    solve()