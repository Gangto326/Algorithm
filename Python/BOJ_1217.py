import sys
sys.setrecursionlimit(41_000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    while True:
        N, M = int(next(iterator)), int(next(iterator))

        if N == 0 and M == 0:
            break

        node_list = [[] for _ in range(M * 2 + 1)]
        reversed_node_list = [[] for _ in range(M * 2 + 1)]

        for _ in range(N):
            first, sec = int(next(iterator)), int(next(iterator))

            node_list[first + M if first > 0 else -first].append(sec if sec > 0 else -sec + M)
            reversed_node_list[sec if sec > 0 else -sec + M].append(first + M if first > 0 else -first)

            node_list[sec + M if sec > 0 else -sec].append(first if first > 0 else -first + M)
            reversed_node_list[first if first > 0 else -first + M].append(sec + M if sec > 0 else -sec)
        
        stack = []
        check = [True] * (M * 2 + 1)


        def DFS(index):
            check[index] = False

            for node in node_list[index]:
                if check[node]:
                    DFS(node)
            
            stack.append(index)
        

        for i in range(1, M * 2 + 1):
            if check[i]:
                DFS(i)
        
        groups = [0] * (M * 2 + 1)
        group_id = 0


        def reversed_DFS(index, group_id):
            groups[index] = group_id

            for node in reversed_node_list[index]:
                if not groups[node]:
                    reversed_DFS(node, group_id)
        

        while stack:
            node = stack.pop()

            if not groups[node]:
                group_id += 1
                reversed_DFS(node, group_id)

        answer = 1
        for i in range(1, M + 1):
            if groups[i] == groups[i + M]:
                answer = 0
                break

        print(answer)


if __name__ == "__main__":
    solve()