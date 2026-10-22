import sys
sys.setrecursionlimit(200_000)

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    node_list = [set() for _ in range(N + 1)]

    for _ in range(M):
        start, end = map(int, read().split())
        node_list[start].add(end)
        node_list[end].add(start)
    
    for i in range(N + 1):
        node_list[i] = list(sorted(list(node_list[i])))
    
    check = [True] * (N + 1)
    check[1] = False
    answer = [1]

    def DFS(index):
        nonlocal node_list, check, answer

        for next_node in node_list[index]:
            if check[next_node]:
                check[next_node] = False
                answer.append(next_node)
                DFS(next_node)
    
    DFS(1)
    print(*answer)


if __name__ == "__main__":
    solve()