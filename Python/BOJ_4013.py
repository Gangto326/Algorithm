import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    
    node_list = [[] for _ in range(N + 1)]
    reversed_node_list = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, read().split())
        node_list[start].append(end)
        reversed_node_list[end].append(start)
    
    stack = []
    check = [True] * (N + 1)
    edge_idx = [0] * (N + 1)

    for i in range(1, N + 1):
        if check[i]:
            call_stack = [i]
            check[i] = False
            
            while call_stack:
                curr = call_stack[-1]
                
                while edge_idx[curr] < len(node_list[curr]):
                    next_node = node_list[curr][edge_idx[curr]]
                    edge_idx[curr] += 1
                    
                    if check[next_node]:
                        check[next_node] = False
                        call_stack.append(next_node)
                        break
                else:
                    stack.append(call_stack.pop())
    
    groups = [0] * (N + 1)
    group_id = 0
    reversed_edge_idx = [0] * (N + 1)

    while stack:
        start_node = stack.pop()

        if not groups[start_node]:
            group_id += 1
            call_stack = [start_node]
            groups[start_node] = group_id
            
            while call_stack:
                curr = call_stack[-1]
                
                while reversed_edge_idx[curr] < len(reversed_node_list[curr]):
                    next_node = reversed_node_list[curr][reversed_edge_idx[curr]]
                    reversed_edge_idx[curr] += 1
                    
                    if not groups[next_node]:
                        groups[next_node] = group_id
                        call_stack.append(next_node)
                        break
                else:
                    call_stack.pop()
    
    group_cost = [0] * (group_id + 1)
    for i in range(1, N + 1):
        group_cost[groups[i]] += int(read())

    group_edge_list = [set() for _ in range(group_id + 1)]
    indgree = [0] * (group_id + 1)
    
    for i in range(1, N + 1):
        for end in node_list[i]:
            if groups[i] != groups[end]:
                if groups[end] not in group_edge_list[groups[i]]:
                    group_edge_list[groups[i]].add(groups[end])
                    indgree[groups[end]] += 1

    start_node, restaurant_num = map(int, read().split())
    start_node = groups[start_node]

    restaurant = [False] * (group_id + 1)
    restaurant_list = list(map(int, read().split()))
    for i in range(restaurant_num):
        restaurant[groups[restaurant_list[i]]] = True

    DP = [0] * (group_id + 1)
    DP[start_node] = -group_cost[start_node]

    is_start = [False] * (group_id + 1)
    is_start[start_node] = True

    BFS = deque()
    for i in range(1, group_id + 1):
        if not indgree[i]:
            BFS.append(i)
    
    while BFS:
        node = BFS.popleft()

        for next_node in group_edge_list[node]:
            if is_start[node]:
                DP[next_node] = min(DP[next_node], DP[node] - group_cost[next_node])
                is_start[next_node] = True

            indgree[next_node] -= 1

            if not indgree[next_node]:
                BFS.append(next_node)

    answer = 0
    for i in range(1, group_id + 1):
        if restaurant[i]:
            answer = max(answer, -DP[i])
    print(answer)
    

if __name__ == "__main__":
    solve()