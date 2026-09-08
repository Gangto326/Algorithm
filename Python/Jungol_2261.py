import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    
    node_list = [None] + [int(read().strip(), base=2) for _ in range(N)]
    check = [True] * (N + 1)

    start, end = map(int, read().split())

    BFS = deque()
    BFS.append(start)
    check[start] = False

    route = [i for i in range(N + 1)]

    while BFS:
        index = BFS.popleft()

        if index == end:
            break

        for i in range(1, N + 1):
            if check[i]:
                if bin(node_list[i] ^ node_list[index]).count('1') == 1:
                    check[i] = False
                    route[i] = index
                    BFS.append(i)

    if route[end] == end:
        print(-1)
        return

    start_index = end
    answer = [end]
    
    while True:
        start_index = route[start_index]
        answer.append(start_index)

        if start_index == start:
            break
    
    answer.reverse()
    print(*answer)


if __name__ == "__main__":
    solve()