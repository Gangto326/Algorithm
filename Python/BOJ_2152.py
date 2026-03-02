import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M, S, T = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))
    node_list = [[] for _ in range(N + 1)]
    reversed_node_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = int(next(iterator)), int(next(iterator))
        node_list[A].append(B)
        reversed_node_list[B].append(A)

    check = [True] * (N + 1)
    stack = []
    

    def DFS(index):
        check[index] = False

        for node in node_list[index]:
            if check[node]:
                DFS(node)
        
        stack.append(index)


    for i in range(1, N + 1):
        if check[i]:
            DFS(i)

    
    groups = [0] * (N + 1)
    group_id = 0


    def reversed_DFS(index, group_id):
        groups[index] = group_id

        for node in reversed_node_list[index]:
            if not groups[node]:
                reversed_DFS(node, group_id)
    

    while stack:
        index = stack.pop()

        if not groups[index]:
            group_id += 1
            reversed_DFS(index, group_id)
    
    next_groups = [set() for _ in range(group_id + 1)]
    for start in range(1, N + 1):
        for end in node_list[start]:
            if groups[start] != groups[end]:
                next_groups[groups[start]].add(groups[end])

    group_count = defaultdict(int)
    for i in range(1, N + 1):
        group_count[groups[i]] += 1

    memo = [-1] * (group_id + 1)


    def find_answer(g_index, end_index):
        if not memo[g_index] == -1:
            return memo[g_index]
        
        if g_index == end_index:
            memo[g_index] = group_count[end_index]
            return memo[g_index]

        max_count = -float('inf')

        for g in next_groups[g_index]:
            if g_index == g:
                continue

            max_count = max(max_count, find_answer(g, end_index))
        
        memo[g_index] = max_count + group_count[g_index]
        return memo[g_index]
    

    answer = find_answer(groups[S], groups[T])
    print(answer if answer != -float('inf') else 0)


if __name__ == "__main__":
    solve()