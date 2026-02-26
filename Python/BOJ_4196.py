import sys
sys.setrecursionlimit(10 ** 6)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))

    for tc in range(T):
        N, M = int(next(iterator)), int(next(iterator))

        next_nodes = [[] for _ in range(N + 1)]
        reversed_nodes = [[] for _ in range(N + 1)]
        for _ in range(M):
            x, y = int(next(iterator)), int(next(iterator))
            next_nodes[x].append(y)
            reversed_nodes[y].append(x)
        
        
        visited = [False] * (N + 1)
        stack = []


        def DFS(index):
            visited[index] = True

            for node in next_nodes[index]:
                if not visited[node]:
                    DFS(node)
            
            stack.append(index)
        

        for i in range(1, N + 1):
            if not visited[i]:
                DFS(i)

        visited = [False] * (N + 1)
        node_group = [0] * (N + 1)
        group_id = 0
        

        def reversed_DFS(index, group_id):
            visited[index] = True
            node_group[index] = group_id

            for node in reversed_nodes[index]:
                if not visited[node]:
                    reversed_DFS(node, group_id)
        

        while stack:
            i = stack.pop()

            if not visited[i]:
                group_id += 1
                reversed_DFS(i, group_id)
        

        in_degree = [0] * (group_id + 1)
        for i in range(1, N + 1):
            for node in next_nodes[i]:
                if node_group[i] != node_group[node]:
                    in_degree[node_group[node]] += 1
        
        answer = 0
        for i in range(1, group_id + 1):
            if not in_degree[i]:
                answer += 1
        
        print(answer)


if __name__ == "__main__":
    solve()