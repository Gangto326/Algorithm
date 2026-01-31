import sys
from collections import deque
sys.setrecursionlimit(10**6)

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    M = int(read().rstrip())
    next_nodes = [[] for _ in range(10010)]
    count_list = [0] * 10010
    total_cost = [0] * 10010
    before_node = [[] for _ in range(10010)]

    for _ in range(M):
        start, end, cost = map(int, read().split())

        next_nodes[start].append((end, cost))
        count_list[end] += 1
    
    start, end = map(int, read().split())
    BFS = deque([start])

    while BFS:
        node = BFS.popleft()

        for next_node, cost in next_nodes[node]:

            if total_cost[next_node] < total_cost[node] + cost:
                total_cost[next_node] = total_cost[node] + cost
                before_node[next_node] = [node]
            elif total_cost[next_node] == total_cost[node] + cost:
                before_node[next_node].append(node)           

            count_list[next_node] -= 1

            if not count_list[next_node]:
                BFS.append(next_node)
    
    print(total_cost[end])
    
    count = 0
    check = set()
    def DFS(index, start):
        nonlocal count

        if index == start:
            return
        
        for before in before_node[index]:
            if not (index, before) in check and not (before, index) in check:
                count += 1
                check.add((index, before))
                check.add((before, index))
                # print(index, "  to. ", before)
                DFS(before, start)

    DFS(end, start)
    print(count)

if __name__ == "__main__":
    solve()