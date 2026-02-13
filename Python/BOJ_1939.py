import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    heap = []
    for _ in range(M):
        start, end, cost = map(int, read().split())
        heapq.heappush(heap, (-cost, start, end))
    
    parents = [i for i in range(N+1)]
    start, end = map(int, read().split())


    def find(index):
        if parents[index] == index:
            return index

        parents[index] = find(parents[index])
        return parents[index]


    def union(a, b):
        pa = find(a)
        pb = find(b)

        if pa == pb:
            return True
        
        parents[pa] = pb
        return False
    

    answer = float('inf')
    while heap:
        cost, a, b = heapq.heappop(heap)
        answer = -cost
        union(a, b)

        if find(start) ==  find(end):
            print(answer)
            return


if __name__ == "__main__":
    solve()