import sys
from collections import deque

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))

    node_list = [[] for _ in range(N+1)]
    count_list = [0] * (N+1)
    day_list = [1] * (N+1)

    for _ in range(M):
        start, end = int(next(iterator)), int(next(iterator))
        node_list[start].append(end)
        count_list[end] += 1
    
    BFS = deque()
    for i in range(1, N+1):
        if not count_list[i]:
            BFS.append(i)
    
    while BFS:
        node = BFS.popleft()

        for next_node in node_list[node]:
            count_list[next_node] -= 1
            day_list[next_node] = max(day_list[next_node], day_list[node] + 1)

            if not count_list[next_node]:
                BFS.append(next_node)
    
    print(*day_list[1:])


if __name__ == "__main__":
    solve()