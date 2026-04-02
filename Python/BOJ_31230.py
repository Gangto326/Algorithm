import sys, heapq
sys.setrecursionlimit(200_010)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M, A, B = int(next(iterator)), int(next(iterator)), int(next(iterator)), int(next(iterator))
    node_list = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, cost = int(next(iterator)), int(next(iterator)), int(next(iterator))

        node_list[a].append((b, cost))
        node_list[b].append((a, cost))
    
    dijkstra = []
    heapq.heappush(dijkstra, (0, A))

    check = [float('inf')] * (N + 1)
    check[A] = 0

    root_list = [[] for _ in range(N + 1)]
    while dijkstra:
        total, node = heapq.heappop(dijkstra)

        if check[node] < total:
            continue

        if node == B:
            continue

        if check[B] < total:
            break

        for next_node, next_cost in node_list[node]:
            next_total = total + next_cost

            if check[next_node] > next_total:
                check[next_node] = next_total
                root_list[next_node] = []
                root_list[next_node].append(node)
                heapq.heappush(dijkstra, (next_total, next_node))
            
            elif check[next_node] == next_total:
                root_list[next_node].append(node)
                
    answer_set = {B}
    check = [True] * (N + 1)
    stack = []
    stack.append(B)

    while stack:
        node = stack.pop()

        if node == A:
            continue

        check[node] = False

        for next_node in root_list[node]:
            if check[next_node]:
                answer_set.add(next_node)
                stack.append(next_node)

    print(len(answer_set))
    print(*sorted(list(answer_set)))


if __name__ == "__main__":
    solve()