import sys
sys.setrecursionlimit(200000)

def solve():
    read = sys.stdin.readline
    N, R, Q = map(int, read().split())
    node_list = [[] for _ in range(N+1)]

    for _ in range(N-1):
        start, end = map(int, read().split())
        
        node_list[start].append(end)
        node_list[end].append(start)

    child_list = [0] * (N+1)


    def DFS(index, parents):
        nonlocal node_list, child_list

        count = 1
        for child in node_list[index]:
            if child != parents:
                count += DFS(child, index)
        
        child_list[index] = count
        return count


    DFS(R, -1)
    for _ in range(Q):
        print(child_list[int(read().rstrip())])


if __name__ == "__main__":
    solve()