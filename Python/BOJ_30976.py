import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    G = list(map(int, read().split()))
    B = list(map(int, read().split()))
    L = list(map(int, read().split()))
    U = list(map(int, read().split()))

    node_list = [[] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if B[j] < L[i] and G[i] > U[j]:
                node_list[i].append(j)
                
    match = [-1] * M
    

    def DFS(index, visited):
        if not visited[index]:
            return False
        
        visited[index] = False

        for next_node in node_list[index]:
            if match[next_node] == -1 or DFS(match[next_node], visited):
                match[next_node] = index
                return True
            
        return False


    answer = 0
    for i in range(N):
        visited = [True] * N

        if DFS(i, visited):
            answer += 1
            
    print(answer)


if __name__ == "__main__":
    solve()