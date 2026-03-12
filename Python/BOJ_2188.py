import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    N, M = int(next(iterator)), int(next(iterator))
    node_list = [[] for _ in range(N + 1)]
    house = [0] * (M + 1)

    for i in range(1, N + 1):
        num = int(next(iterator))

        for j in range(num):
            node_list[i].append(int(next(iterator)))
    

    def DFS(index, check):
        if check[index]:
            return False

        check[index] = True
        
        for node in node_list[index]:
            if house[node] == 0 or DFS(house[node], check):
                house[node] = index
                return True
        
        return False
    

    answer = 0
    for i in range(1, N + 1):
        if DFS(i, [False] * (N + 1)):
            answer += 1
    
    print(answer)


if __name__ == "__main__":
    solve()