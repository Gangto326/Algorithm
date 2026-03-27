import sys
sys.setrecursionlimit(200_010)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N = int(next(iterator))
    parents = [i for i in range(N + 1)]
    indegree = [0] * (N + 1)


    def find(index):
        if parents[index] == index:
            return index
        
        parents[index] = find(parents[index])
        return parents[index]


    def union(a, b):
        ap = find(a)
        bp = find(b)

        if ap != bp:
            parents[ap] = bp


    for _ in range(N):
        up, down = int(next(iterator)), int(next(iterator))

        union(up, down)
        indegree[down] += 1
    
    indegree_count = [0] * (N + 1)
    group_count = [0] * (N + 1)

    for i in range(1, N + 1):
        parent = find(i)
        group_count[parent] += 1
        
        if indegree[i] == 0:
            indegree_count[parent] += 1
    
    answer = 0
    for i in range(1, N + 1):
        if parents[i] == i:

            if group_count[i] != 1:
                answer += group_count[i] + 1

            if indegree_count[i] >= 2:
                print(-1)
                return
    
    print(answer)


if __name__ == "__main__":
    solve()