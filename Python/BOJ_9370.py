import sys, heapq

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    T = int(next(iterator))

    for tc in range(T):
        n, m, t = int(next(iterator)), int(next(iterator)), int(next(iterator))
        start, g, h = int(next(iterator)), int(next(iterator)), int(next(iterator))

        node_list = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b, d = int(next(iterator)), int(next(iterator)), int(next(iterator))
            node_list[a].append((b, d))
            node_list[b].append((a, d))
        
        end_set = set()
        for _ in range(t):
            end_set.add(int(next(iterator)))

        dijkstra = []
        heapq.heappush(dijkstra, (0, start, False))

        min_cost = [float('inf')] * (n+1)
        min_cost[start] = 0
        check = [False] * (n+1)
        
        while dijkstra:
            cost, index, smell = heapq.heappop(dijkstra)

            if min_cost[index] < cost:
                continue

            for next_node, c in node_list[index]:
                next_cost = cost + c

                if min_cost[next_node] < next_cost:
                    continue

                is_smell = smell
                if (index == g and next_node == h) or (index == h and next_node == g):
                    is_smell = True

                if min_cost[next_node] == next_cost:
                    if check[next_node] or not is_smell:
                        continue

                    check[next_node] = is_smell
                    
                elif min_cost[next_node] > next_cost:
                    check[next_node] = is_smell

                heapq.heappush(dijkstra, (next_cost, next_node, is_smell))
                min_cost[next_node] = next_cost

        answer_list = []
        for i in range(1, n+1):
            if check[i] and i in end_set:
                answer_list.append(i)

        print(*answer_list)


if __name__ == "__main__":
    solve()