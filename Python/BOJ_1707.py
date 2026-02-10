import sys
from collections import deque

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))

    for tc in range(T):
        V, E = int(next(iterator)), int(next(iterator))
        node_list = [[] for _ in range(V+1)]

        for _ in range(E):
            start, end = int(next(iterator)), int(next(iterator))
            node_list[start].append(end)
            node_list[end].append(start)

        flag = True
        node_count = 0
        check = [0] * (V+1)
        while node_count != V:
            if not flag:
                break

            BFS = deque()
            start_node = 0
            for i in range(1, V+1):
                if not check[i]:
                    start_node = i
                    break
            
            BFS.append((start_node, 1))
            check[start_node] = 1
            node_count += 1

            while BFS:
                node, count = BFS.popleft()

                count += 1
                for next_node in node_list[node]:
                    if not flag:
                        break
                    
                    if check[next_node] and ((check[node] == check[next_node] + 2) or (check[node] == check[next_node])):
                        flag = False
                        break

                    if not check[next_node]:
                        node_count += 1
                        check[next_node] = count
                        BFS.append((next_node, count))

                if not flag:
                    break

        if flag:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()