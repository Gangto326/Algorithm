import sys
sys.setrecursionlimit(200_010)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))

    node_list = [[] for _ in range(N + 1)]
    reversed_node_list = [[] for _ in range(N + 1)]
    edge_list = []

    for _ in range(M):
        start, end = int(next(iterator)), int(next(iterator))
        node_list[start].append(end)
        reversed_node_list[end].append(start)
        edge_list.append((start, end))

    stack = []
    check = [True] * (N + 1)


    def DFS(index):
        check[index] = False

        for next_node in node_list[index]:
            if check[next_node]:
                DFS(next_node)
        
        stack.append(index)
    

    for i in range(1, N + 1):
        if check[i]:
            DFS(i)
    
    groups = [0] * (N + 1)
    group_id = 0


    def reversed_DFS(index, group_id):
        groups[index] = group_id

        for next_node in reversed_node_list[index]:
            if not groups[next_node]:
                reversed_DFS(next_node, group_id)
    

    while stack:
        node = stack.pop()

        if not groups[node]:
            group_id += 1
            reversed_DFS(node, group_id)
    
    connected = [False] * group_id
    for start, end in edge_list:
        if groups[start] != groups[end]:
            if groups[end] == groups[start] + 1:
                connected[groups[start]] = True

    for i in range(1, group_id):
        if not connected[i]:
            print(0)
            return
    
    answer_list = []
    for i in range(N + 1):
        if groups[i] == 1:
            answer_list.append(i)
    
    print(len(answer_list))
    print(*answer_list)


if __name__ == "__main__":
    solve()