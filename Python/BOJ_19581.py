import sys
sys.setrecursionlimit(200000)

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    answer = -float('inf')

    node_list = [[] for _ in range(N+1)]
    vertax_list = []
    for i in range(N-1):
        first, sec, cost = map(int, read().split())
        node_list[first].append((sec, cost))
        node_list[sec].append((first, cost))

    start_node = 0
    max_length = 0
    check = [True] * (N+1)
    check[1] = False

    def DFS(node, total, mark):
        nonlocal start_node, max_length, check, node_list

        for next_node, cost in node_list[node]:
            if next_node == mark:
                continue

            if check[next_node]:
                check[next_node] = False
                next_total = total+cost

                if max_length < next_total:
                    max_length = next_total
                    start_node = next_node

                DFS(next_node, next_total, mark)
                check[next_node] = True

    DFS(1, 0, -1)
    vertax_list.append(start_node)
    check[1] = True
    check[start_node] = False
    max_length = 0

    DFS(start_node, 0, -1)
    vertax_list.append(start_node)
    check[vertax_list[0]] = True

    max_length = 0
    check[vertax_list[0]] = False
    DFS(vertax_list[0], 0, vertax_list[1])
    answer = max(answer, max_length)
    check[vertax_list[0]] = True

    max_length = 0
    check[vertax_list[1]] = False
    DFS(vertax_list[1], 0, vertax_list[0])
    answer = max(answer, max_length)

    print(answer)


if __name__ == "__main__":
    solve()