import sys
sys.setrecursionlimit(20_000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))

    node_list = [[] for _ in range(N * 2 + 1)]
    reversed_node_list = [[] for _ in range(N * 2 + 1)]

    for _ in range(M):
        first, sec = int(next(iterator)), int(next(iterator))

        node_list[first + N if first > 0 else -first].append(sec if sec > 0 else -sec + N)
        reversed_node_list[sec if sec > 0 else -sec + N].append(first + N if first > 0 else -first)

        node_list[sec + N if sec > 0 else -sec].append(first if first > 0 else -first + N)
        reversed_node_list[first if first > 0 else -first + N].append(sec + N if sec > 0 else -sec)
    
    stack = []
    check = [True] * (N * 2 + 1)


    def DFS(index):
        check[index] = False

        for node in node_list[index]:
            if check[node]:
                DFS(node)
        
        stack.append(index)
    

    for i in range(1, N * 2 + 1):
        if check[i]:
            DFS(i)
    
    groups = [0] * (N * 2 + 1)
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
    answer_list = []

    for i in range(1, N + 1):
        if groups[i] == groups[i + N]:
            answer = 0
            break
        
        elif groups[i] < groups[i + N]:
            answer_list.append(0)
        
        else:
            answer_list.append(1)
    
    if not answer:
        print(answer)
    else:
        print(answer)
        print(*answer_list)


if __name__ == "__main__":
    solve()