import sys, heapq

def solve():
    read = sys.stdin.buffer.readline
    N = int(read())
    num_list = [int(read()) for _ in range(N)]
    parents = [i for i in range(N + 1)]
    heap = []

    for i in range(N):
        cost_list = list(map(int, read().split()))

        for j in range(i + 1, N):
            cost = cost_list[j]

            if i != j:
                heapq.heappush(heap, (cost, i, j))
    
    for i in range(N):
        heapq.heappush(heap, (num_list[i], N, i))
    

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
    

    answer = 0
    while heap:
        cost, a, b = heapq.heappop(heap)

        if union(a, b):
            answer += cost

    print(answer)


if __name__ == "__main__":
    solve()