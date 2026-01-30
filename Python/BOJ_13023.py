import sys
sys.setrecursionlimit(10**6)

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    node_list = [[] for _ in range(N)]
    check = [True] * N

    for _ in range(M):
        a, b = map(int, read().split())
        node_list[a].append(b)
        node_list[b].append(a)


    def DFS(index, count):
        if count == 5:
            print(1)
            sys.exit()

        for next_node in node_list[index]:
            if check[next_node]:
                check[next_node] = False
                DFS(next_node, count+1)
                check[next_node] = True
    

    for i in range(N):
        if node_list[i]:
            check[i] = False
            DFS(i, 1)
            check[i] = True

    print(0)


if __name__ == "__main__":
    solve()