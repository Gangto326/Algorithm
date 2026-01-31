import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    next_list = [[] for _ in range(N+1)]
    count_list = [0] * (N+1)
    cost_list = [0] * (N+1)
    total_cost = [0] * (N+1)

    for i in range(N):
        num_list = list(map(int, read().split()))
        cost_list[i+1] = num_list[0]
        index = 1

        while num_list[index] != -1:
            next_list[num_list[index]].append(i+1)
            count_list[i+1] += 1
            index += 1

    BFS = deque()
    for i in range(1, N+1):
        if count_list[i] == 0:
            BFS.append(i)
    
    while BFS:
        node = BFS.popleft()

        for next_node in next_list[node]:
            total_cost[next_node] = max(total_cost[next_node], total_cost[node] + cost_list[node])
            count_list[next_node] -= 1

            if not count_list[next_node]:
                BFS.append(next_node)
    
    for i in range(1, N+1):
        print(cost_list[i] + total_cost[i])


if __name__ == "__main__":
    solve()