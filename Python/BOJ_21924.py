import sys, heapq
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    total = 0
    heap = []

    for _ in range(M):
        start, end, cost = map(int, read().split())
        heapq.heappush(heap, (cost, start, end))
        total += cost

    parents = [i for i in range(N + 1)]

    
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
    

    count = 1
    while heap:
        cost, a, b = heapq.heappop(heap)

        if union(a, b):
            total -= cost
            count += 1

        if count == N:
            break

    if count == N:
        print(total)
    else:
        print(-1)


if __name__ == "__main__":
    solve()