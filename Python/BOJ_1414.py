import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    heap = []
    parents = [i for i in range(N + 1)]

    total = 0
    for i in range(1, N + 1):
        row = read().rstrip()

        for j in range(N):
            length = ord(row[j]) - 96

            if length < 0:
                length += 31
                length += 27

                if length == 10:
                    continue

            total += length
            heapq.heappush(heap, (length, i, j+1))
    

    def find(index):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]
    

    def union(a, b):
        a_parent = find(a)
        b_parent = find(b)

        if a_parent == b_parent:
            return False
        
        parents[b_parent] = a_parent
        return True


    count = 1
    mst = 0
    while heap:
        length, a, b = heapq.heappop(heap)

        if union(a, b):
            mst += length
            count += 1

        if count == N:
            break
        
    if count == N:
        print(total - mst)
    else:
        print(-1)


if __name__ == "__main__":
    solve()