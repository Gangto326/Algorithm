import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    parents = [i for i in range(N + 1)]
    min_heap = []
    max_heap = []
    
    q, w, c = map(int, read().split())
    if not c:
        c = 1
    else:
        c = 0

    for _ in range(M):
        A, B, C = map(int, read().split())

        if not C:
            C = 1
        else:
            C = 0

        heapq.heappush(min_heap, (C, A, B))
        heapq.heappush(max_heap, (-C, A, B))


    def find(index):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]
    

    def union(a, b):
        ap = find(a)
        bp = find(b)

        if ap == bp:
            return False
        
        parents[ap] = bp
        return True
    

    min_count = 1
    min_answer = c

    while min_heap:
        cost, a, b = heapq.heappop(min_heap)

        if union(a, b):
            min_count += 1
            min_answer += cost

        if min_count == N:
            break

    max_count = 1
    max_answer = -c
    parents = [i for i in range(N + 1)]

    while max_heap:
        cost, a, b = heapq.heappop(max_heap)

        if union(a, b):
            max_count += 1
            max_answer += cost

        if max_count == N:
            break
    

    print((max_answer ** 2) - (min_answer ** 2))


if __name__ == "__main__":
    solve()