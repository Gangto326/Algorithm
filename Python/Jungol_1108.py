import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    E = int(read())
    node_set = set()
    next_node_list = [[] for _ in range(501)]
    N = 0

    for _ in range(E):
        x, y = map(int, read().split())
        node_set.add(x)
        node_set.add(y)
        next_node_list[x].append(y)
        N = max(N, x, y)

    total = 0
    count = 0

    for node in node_set:
        check = [True] * (N + 1)
        check[node] = False

        BFS = deque()
        BFS.append((node, 0))

        while BFS:
            n, c = BFS.popleft()
            
            for next_node in next_node_list[n]:
                if check[next_node]:
                    check[next_node] = False
                    total += c + 1
                    count += 1
                    BFS.append((next_node, c + 1))
        
    print(f"{round(total / count, 3):.3f}")


if __name__ == "__main__":
    solve()