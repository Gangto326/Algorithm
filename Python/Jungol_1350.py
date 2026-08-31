import sys, heapq

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    parents = [i for i in range(N + 1)]

    heap = []
    for _ in range(M):
        a, b, cost = map(int, read().split())
        heapq.heappush(heap, (-cost, a, b))
    
    
    def find(index):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]
    

    def union(first, sec):
        fp = find(first)
        sp = find(sec)

        if fp == sp:
            return False
        
        parents[fp] = sp
        return True


    count = 1
    answer = 0
    while heap:
        cost, a, b = heapq.heappop(heap)

        if union(a, b):
            count += 1
            answer -= cost

        if count == N:
            break

    print(answer)


if __name__ == "__main__":
    solve()