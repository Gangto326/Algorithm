import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    parents = [i for i in range(N + 1)]
    heap = []

    for i in range(N):
        li = list(map(int, read().split()))

        for j in range(N):
            if i == j:
                continue

            heapq.heappush(heap, (li[j], i + 1, j + 1))

    
    def find(index):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]
    

    def union(a, b):
        a_p = find(a)
        b_p = find(b)

        if a_p == b_p:
            return False
        
        parents[a_p] = b_p
        return True

    
    count = 1
    answer = 0
    while heap:
        cost, a, b = heapq.heappop(heap)

        if union(a, b):
            count += 1
            answer += cost
        
        if count == N:
            break

    print(answer)


if __name__ == "__main__":
    solve()