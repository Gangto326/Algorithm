import sys, heapq

def solve():
    read = sys.stdin.readline
    N = int(read())
    board = [list(map(int, read().split())) for _ in range(N)]
    parents = [i for i in range(N)]

    heap = []
    for i in range(N):
        for j in range(i + 1, N):
            heapq.heappush(heap, (board[i][j], i, j))
    

    def find(index):
        if index == parents[index]:
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
    count = 1
    while count < N and heap:
        cost, a, b = heapq.heappop(heap)

        if union(a, b):
            answer += cost
            count += 1

    print(answer)


if __name__ == "__main__":
    solve()