import sys, heapq

def solve():
    read = sys.stdin.readline
    V, E, P = map(int, read().split())
    edge_list = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end, cost = map(int, read().split())
        edge_list[start].append((end, cost))
        edge_list[end].append((start, cost))

    heap = []
    heapq.heappush(heap, (0, 1, True if P == 1 else False))

    check = [float('inf')] * (V+1)
    check[1] = 0

    max_cost = float('inf')
    flag = False
    while heap:
        cost, node, f = heapq.heappop(heap)

        if cost > max_cost:
            break

        if node == V:
            if max_cost > cost:
                max_cost = cost
                flag = f

            elif max_cost == cost:
                flag = flag | f

            continue

        for next_node in edge_list[node]:
            index, n_cost = next_node
            total = cost + n_cost

            if check[index] >= total:
                check[index] = total

                if index == P:
                    heapq.heappush(heap, (total, index, True))
                
                else:
                    heapq.heappush(heap, (total, index, f))

    print("SAVE HIM" if flag else "GOOD BYE")


if __name__ == "__main__":
    solve()