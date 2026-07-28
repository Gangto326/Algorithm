import sys
sys.setrecursionlimit(2000)

def solve():
    read = sys.stdin.read()
    iterator = iter(read.split())


    def DFS(node, parents, min_cost):
        total = 0
        for end, cost in node_list[node]:
            if end != parents:
                total += DFS(end, node, cost)
        
        if total == 0:
            return min_cost
        
        return min(total, min_cost)
    

    while True:
        N, R = int(next(iterator)), int(next(iterator))
        if N == R == 0:
            break

        node_list = [[] for _ in range(N + 1)]

        for _ in range(N - 1):
            start, end, cost = int(next(iterator)), int(next(iterator)), int(next(iterator))
            node_list[start].append((end, cost))
            node_list[end].append((start, cost))

        answer = DFS(R, 0, float('inf'))
        print(answer if answer != float('inf') else 0)


if __name__ == "__main__":
    solve()