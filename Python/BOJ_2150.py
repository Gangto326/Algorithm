import sys
sys.setrecursionlimit(10 ** 6)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    V, E = int(next(iterator)), int(next(iterator))

    node_list = [[] for _ in range(V + 1)]
    reversed_node_list = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = int(next(iterator)), int(next(iterator))
        node_list[start].append(end)
        reversed_node_list[end].append(start)
    
    visited = [True] * (V + 1)
    stack = []


    def DFS(index):
        visited[index] = False

        for node in node_list[index]:
            if visited[node]:
                DFS(node)
        
        stack.append(index)
    

    for i in range(1, V + 1):
        if visited[i]:
            DFS(i)
    
    group_list = [0] * (V + 1)
    group_id = 0


    def reversed_DFS(index, group_id):
        group_list[index] = group_id

        for node in reversed_node_list[index]:
            if not group_list[node]:
                reversed_DFS(node, group_id)
        

    while stack:
        index = stack.pop()

        if not group_list[index]:
            group_id += 1
            reversed_DFS(index, group_id)

    answer_list = [[] for _ in range(group_id)]
    for i in range(1, V + 1):
        answer_list[group_list[i]-1].append(i)
    
    answer_list.sort(key = lambda x: x[0])

    print(group_id)
    for answer in answer_list:
        print(*answer, -1)


if __name__ == "__main__":
    solve()