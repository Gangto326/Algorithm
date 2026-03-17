import sys
sys.setrecursionlimit(2000)

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    while True:
        try:
            N, M = int(next(iterator)), int(next(iterator))
        except StopIteration:
            return
        
        node_list = [[] for _ in range(N * 2 + 1)]
        reversed_node_list = [[] for _ in range(N * 2 + 1)]

        for _ in range(M):
            query = next(iterator)
            first_query = query[0]
            first_num = int(query[1:])

            query = next(iterator)
            sec_query = query[0]
            sec_num = int(query[1:])

            if first_query == sec_query:
                if first_query == "+":
                    node_list[first_num + N].append(sec_num)
                    reversed_node_list[sec_num].append(first_num + N)

                    node_list[sec_num + N].append(first_num)
                    reversed_node_list[first_num].append(sec_num + N)
                
                else:
                    node_list[first_num].append(sec_num + N)
                    reversed_node_list[sec_num + N].append(first_num)

                    node_list[sec_num].append(first_num + N)
                    reversed_node_list[first_num + N].append(sec_num)
            
            else:
                if first_query == "+":
                    node_list[first_num + N].append(sec_num + N)
                    reversed_node_list[sec_num + N].append(first_num + N)

                    node_list[sec_num].append(first_num)
                    reversed_node_list[first_num].append(sec_num)

                else:
                    node_list[first_num].append(sec_num)
                    reversed_node_list[sec_num].append(first_num)

                    node_list[sec_num + N].append(first_num + N)
                    reversed_node_list[first_num + N].append(sec_num + N)
                    
        stack = []
        check = [True] * (N * 2 + 1)


        def DFS(index):
            check[index] = False

            for node in node_list[index]:
                if check[node]:
                    DFS(node)
            
            stack.append(index)
        

        for i in range(1, N * 2 + 1):
            if check[i]:
                DFS(i)
        
        groups = [0] * (N * 2 + 1)
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
        for i in range(1, N + 1):
            if groups[i] == groups[i + N]:
                answer = 0
                break
        
        print(answer)


if __name__ == "__main__":
    solve()