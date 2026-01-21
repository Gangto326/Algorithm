import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, P = map(int, read().split())

    total_nodes = N * 2 + 1
    capacity = [[0] * total_nodes for _ in range(total_nodes)]
    node_list = [[] for _ in range(total_nodes)]


    def add_edge(start, end, cost):
        node_list[start].append(end)
        node_list[end].append(start)
        capacity[start][end] = cost


    for i in range(1, N+1):
        if i == 1 or i == 2:
            add_edge(i, i+N, float('inf'))
        else:
            add_edge(i, i+N, 1)

    for _ in range(P):
        left, right = map(int, read().split())

        left_in = left
        left_out = left + N
        right_in = right
        right_out = right + N

        add_edge(right_out, left_in, 1)
        add_edge(left_out, right_in, 1)

    answer = 0
    start = 1 + N
    end = 2
    while True:
        parents = [-1] * total_nodes
        BFS = deque()
        BFS.append(start)

        while BFS:
            node = BFS.popleft()

            if node == end:
                break

            for next_node in node_list[node]:
                if parents[next_node] == -1 and capacity[node][next_node] > 0:
                    parents[next_node] = node
                    BFS.append(next_node)

        if parents[end] == -1:
            break

        answer += 1
        curr = end
        while curr != start:
            parent = parents[curr]
            capacity[parent][curr] -= 1
            capacity[curr][parent] += 1
            curr = parent

    print(answer)


if __name__ == "__main__":
    solve()