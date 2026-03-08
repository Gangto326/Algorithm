import sys
sys.setrecursionlimit(10 ** 5)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))


    def DFS(index, check, stack, node_list):
        check[index] = False

        for next_node in node_list[index]:
            if check[next_node]:
                DFS(next_node, check, stack, node_list)
        
        stack.append(index)

    
    def reversed_DFS(index, group_list, group_id, reversed_node_list):
        group_list[index] = group_id

        for next_node in reversed_node_list[index]:
            if not group_list[next_node]:
                reversed_DFS(next_node, group_list, group_id, reversed_node_list)
        

    for tc in range(T):
        N, M = int(next(iterator)), int(next(iterator))
        node_list = [[] for _ in range(N)]
        reversed_node_list = [[] for _ in range(N)]
        edge_list = []

        for _ in range(M):
            start, end = int(next(iterator)), int(next(iterator))

            if start == end:
                continue

            node_list[start].append(end)
            reversed_node_list[end].append(start)
            edge_list.append((start, end))

        stack = []
        check = [True] * (N)

        for i in range(N):
            if check[i]:
                DFS(i, check, stack, node_list)

        group_list = [0] * (N)
        group_id = 0

        while stack:
            node = stack.pop()
            
            if not group_list[node]:
                group_id += 1
                reversed_DFS(node, group_list, group_id, reversed_node_list)

        indegree = [0] * (group_id + 1)
        for start, end in edge_list:
            if group_list[start] != group_list[end]:
                indegree[group_list[end]] += 1

        zero_count = 0
        start_index = 0
        for i in range(1, group_id + 1):
            if not indegree[i]:
                zero_count += 1
                start_index = i
            
            if zero_count > 1:
                break
        
        if zero_count == 1:
            answer = ""
            for i in range(N):
                if group_list[i] == start_index:
                    answer += str(i) + "\n"
            print(answer)

        else:
            print("Confused\n")


if __name__ == "__main__":
    solve()