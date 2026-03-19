import sys
sys.setrecursionlimit(200_000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    on_off_list = [0] + [int(next(iterator)) for _ in range(N)]
    switch_list = [[] for _ in range(N + 1)]

    for i in range(1, M + 1):
        for _ in range(int(next(iterator))):
            switch_list[int(next(iterator))].append(i)
    
    node_list = [[] for _ in range(M * 2 + 1)]
    reversed_node_list = [[] for _ in range(M * 2 + 1)]

    for i in range(1, N + 1):
        first, sec = switch_list[i]

        if on_off_list[i]:
            node_list[first].append(sec)
            reversed_node_list[sec].append(first)

            node_list[sec].append(first)
            reversed_node_list[first].append(sec)

            node_list[first + M].append(sec + M)
            reversed_node_list[sec + M].append(first + M)

            node_list[sec + M].append(first + M)
            reversed_node_list[first + M].append(sec + M)
        
        else:
            node_list[first].append(sec + M)
            reversed_node_list[sec + M].append(first)

            node_list[sec].append(first + M)
            reversed_node_list[first + M].append(sec)

            node_list[first + M].append(sec)
            reversed_node_list[sec].append(first + M)

            node_list[sec + M].append(first)
            reversed_node_list[first].append(sec + M)

    stack = []
    check = [True] * (M * 2 + 1)


    def DFS(index):
        check[index] = False

        for node in node_list[index]:
            if check[node]:
                DFS(node)
        
        stack.append(index)
    

    for i in range(1, M * 2 + 1):
        if check[i]:
            DFS(i)
    
    groups = [0] * (M * 2 + 1)
    group_id = 0


    def reversed_DFS(index, group_id):
        groups[index] = group_id

        for node in reversed_node_list[index]:
            if not groups[node]:
                reversed_DFS(node, group_id)
    

    while stack:
        node = stack.pop()

        if not groups[node]:
            group_id += 1
            reversed_DFS(node, group_id)
    
    answer = 1
    for i in range(1, M + 1):
        if groups[i] == groups[i + M]:
            answer = 0
            break
    
    print(answer)
    

if __name__ == "__main__":
    solve()