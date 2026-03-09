import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)


    def DFS(index, check, stack, node_list):
        check[index] = False

        for node in node_list[index]:
            if check[node]:
                DFS(node, check, stack, node_list)
        
        stack.append(index)

    
    def reversed_DFS(index, groups, group_id, reversed_node_list):
        groups[index] = group_id

        for node in reversed_node_list[index]:
            if not groups[node]:
                reversed_DFS(node, groups, group_id, reversed_node_list)

    
    while True:
        try:
            N, M = int(next(iterator)), int(next(iterator))
        
        except StopIteration:
            break
        
        node_list = [[] for _ in range(N * 2 + 1)]
        reversed_node_list = [[] for _ in range(N * 2 + 1)]

        node_list[1 + N].append(1)
        reversed_node_list[1].append(1 + N)

        for _ in range(M):
            P, F = int(next(iterator)), int(next(iterator))
            
            node_list[-P if P < 0 else P + N].append(F if F > 0 else -F + N)
            reversed_node_list[F if F > 0 else -F + N].append(-P if P < 0 else P + N)

            node_list[-F if F < 0 else F + N].append(P if P > 0 else -P + N)
            reversed_node_list[P if P > 0 else -P + N].append(-F if F < 0 else F + N)


        stack = []
        check = [True] * (N * 2 + 1)
        
        for i in range(1, N * 2 + 1):
            if check[i]:
                DFS(i, check, stack, node_list)

        groups = [0] * (N * 2 + 1)
        group_id = 0

        while stack:
            node = stack.pop()

            if not groups[node]:
                group_id += 1
                reversed_DFS(node, groups, group_id, reversed_node_list)
        
        answer = "yes"
        for i in range(1, N + 1):
            if groups[i] == groups[i + N]:
                answer = "no"
                break

        print(answer)


if __name__ == "__main__":
    solve()