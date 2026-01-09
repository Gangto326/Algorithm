import sys
sys.setrecursionlimit(200_000)

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())

    node_list = [[] for _ in range(N+1)]
    for _ in range(N):
        query_list = list(map(int, read().split()))

        start = query_list[0]
        index = 1

        while query_list[index] != -1:
            node_list[start].append(query_list[index])
            index += 1
    
    root = int(read().rstrip())
    count_list = [[0, 0] for _ in range(N+1)]
    count = 0
    check = set()


    def DFS(index):
        nonlocal count_list, count, check
        check.add(index)
        count += 1
        count_list[index][0] = count

        for i in sorted(node_list[index]):
            if not i in check:
                DFS(i)

        count += 1
        count_list[index][1] = count


    DFS(root)

    for i in range(1, N+1):
        start, end = count_list[i]
        print(f"{i} {start} {end}")

if __name__ == "__main__":
    solve()