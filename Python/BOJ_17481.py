import sys

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    matching_dict = {}

    for _ in range(M):
        matching_dict[read().strip()] = 0
    
    node_list = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        query = list(read().split())
        node_list[i] = query[1:]
    
    
    def DFS(index, check):
        if not check[index]:
            return False
        
        check[index] = False

        for next_node in node_list[index]:
            if matching_dict[next_node] == 0 or DFS(matching_dict[next_node], check):
                matching_dict[next_node] = index
                return True
        
        return False
    

    answer = 0
    for i in range(1, N + 1):
        check = [True] * (N + 1)

        if DFS(i, check):
            answer += 1
    
    if answer == N:
        print("YES")
    else:
        print("NO")
        print(answer)


if __name__ == "__main__":
    solve()