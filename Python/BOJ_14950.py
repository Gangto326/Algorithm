import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M, T = int(next(iterator)), int(next(iterator)), int(next(iterator))
    heap = []

    for _ in range(M):
        A, B, cost = int(next(iterator)), int(next(iterator)), int(next(iterator))
        heapq.heappush(heap, (cost, A, B))
    
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
    

    count = 0
    answer = 0
    while heap:
        cost, a, b = heapq.heappop(heap)

        if union(a, b):
            answer += cost + (T * count)
            count += 1
        
        if count + 1 == N:
            break

    print(answer)


if __name__ == "__main__":
    solve()