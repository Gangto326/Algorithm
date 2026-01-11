import sys
sys.setrecursionlimit(10**6)

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    status = list(read().rstrip())

    node_list = [[] for _ in range(N+1)]
    check = [False] * (N+1)

    for i in range(N):
        if status[i] == "1":
            check[i+1] = True

    for _ in range(N-1):
        start, end = map(int, read().split())

        node_list[start].append(end)
        node_list[end].append(start)


    def DFS(index, parents):
        nonlocal node_list, check, answer_list

        for i in node_list[index]:
            if i != parents:
                check[index] = not check[index]
                answer_list.append(i)
                DFS(i, index)
            
                if check[i]:
                    check[i] = not check[i]
                    answer_list.append(index)
                else:
                    check[i] = not check[i]
                    check[index] = not check[index]
                    answer_list.extend([index, i, index])
            

    answer_list = []
    DFS(K, 0)

    if check[K]:
        answer_list.append(node_list[K][0])
    
    print(len(answer_list))
    print(*answer_list)
    

if __name__ == "__main__":
    solve()