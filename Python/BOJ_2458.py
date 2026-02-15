import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())

    go_list = [[] for _ in range(N+1)]
    reversed_list = [[] for _ in range(N+1)]

    for _ in range(M):
        start, end = map(int, read().split())

        go_list[start].append(end)
        reversed_list[end].append(start)


    def DFS(index, flag):
        nonlocal count

        if flag:
            for node in go_list[index]:
                if check[node]:
                    check[node] = False
                    count += 1
                    DFS(node, flag)
        
        else:
            for node in reversed_list[index]:
                if check[node]:
                    check[node] = False
                    count += 1
                    DFS(node, flag)


    answer = 0
    for i in range(1, N+1):
        count = 0
        check = [True] * (N+1)
        check[i] = False

        DFS(i, True)
        DFS(i, False)

        if count == (N-1):
            answer += 1
    
    print(answer)


if __name__ == "__main__":
    solve()