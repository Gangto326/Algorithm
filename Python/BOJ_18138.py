import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    node = [0] * (N + 1)
    node_list = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        node[i] = int(next(iterator))

    for j in range(M):
        cara = int(next(iterator))

        for i in range(1, N + 1):
            t = node[i]

            if t/2 <= cara <= (t*3)/4 or t <= cara <= (t*5)/4:
                node_list[i].append(j)
    
    mix_list = [0] * (M + 1)
    check = [True] * (M + 1)


    def DFS(index):
        if not check[index]:
            return False

        check[index] = False

        for i in node_list[index]:
            if mix_list[i] == 0 or DFS(mix_list[i]):
                mix_list[i] = index
                return True
            
        return False


    answer = 0
    for i in range(1, N + 1):
        check = [True] * (N + 1)

        if DFS(i):
            answer += 1
    
    print(answer)


if __name__ == "__main__":
    solve()