import sys
sys.setrecursionlimit(2000)

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    num_list = list(map(int, read().split()))
    node_list = [[] for _ in range(N + 1)]
    reversed_node_list = [[] for _ in range(N + 1)]

    for end in range(1, N + 1):
        start = num_list[end - 1]
        node_list[start].append(end)
        reversed_node_list[end].append(start)
    
    stack = []
    check = [True] * (N + 1)


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
        node = stack.pop()

        if not groups[node]:
            group_id += 1
            reversed_DFS(node, group_id)
    

    count_list = [0] * (group_id + 1)
    for i in range(1, N + 1):
        count_list[groups[i]] += 1

    group_node_list = [[] for _ in range(group_id + 1)]
    indegree = [0] * (group_id + 1)
    for i in range(1, N + 1):
        for node in node_list[i]:
            if groups[i] != groups[node]:
                indegree[groups[node]] += 1
                group_node_list[groups[i]].append(groups[node])

    for i in range(1, group_id + 1):
        if not indegree[i]:
            group_node_list[0].append(i)


    def find_answer(index, max_count):
        DP = [0] * (max_count + 1)
        value = count_list[index]

        for i in range(max_count, value - 1, -1):
            DP[i] = max(DP[i], DP[i - value] + value)

        for next_node in group_node_list[index]:
            before_DP = find_answer(next_node, max_count)

            for i in range(max_count, value - 1, -1):
                for j in range(1, i - value + 1):
                    DP[i] = max(DP[i], DP[i - j] + before_DP[j])
        
        return DP


    print(find_answer(0, K)[-1])


if __name__ == "__main__":
    solve()