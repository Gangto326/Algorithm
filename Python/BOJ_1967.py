import sys
sys.setrecursionlimit(10**6)

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    node_list = [[] for _ in range(N+1)]

    for _ in range(N-1):
        parents, child, cost = map(int, read().split())
        node_list[parents].append((child, cost))
        node_list[child].append((parents, cost))

    start_index = 0
    max_length = 0

    def DFS(index, parents, total_cost):
        nonlocal start_index, max_length

        if len(node_list[index]) == 1:
            if max_length < total_cost:
                start_index = index
                max_length = total_cost
                return

        for next_node, cost in node_list[index]:
            if next_node == parents:
                continue
            else:
                DFS(next_node, index, total_cost+cost)

    DFS(1, -1, 0)
    DFS(start_index, -1, 0)
    print(max_length)


if __name__ == "__main__":
    solve()