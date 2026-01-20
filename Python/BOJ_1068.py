import sys

def solve():
    read = sys.stdin.readline
    N = int(read().rstrip())
    num_list = list(map(int, read().split()))
    node_list = [[] for _ in range(N+1)]

    root = 0
    for i in range(N):
        if num_list[i] == -1:
            root = i
        else:
            node_list[num_list[i]].append(i)
    
    remove_node = int(read().rstrip())
    answer = 0
    if remove_node == root:
        print(0)
        return


    def DFS(index, remove_node):
        nonlocal node_list, answer

        if not node_list[index]:
            answer += 1
            return

        for next_node in node_list[index]:
            if next_node == remove_node:
                if len(node_list[index]) == 1:
                    answer += 1
                continue
            DFS(next_node, remove_node)


    DFS(root, remove_node)
    print(answer)

if __name__ == "__main__":
    solve()