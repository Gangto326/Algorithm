import sys
from collections import deque

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))

    for tc in range(T):
        N = int(next(iterator))
        node_list = [int(next(iterator)) for _ in range(N)]
        next_set = [set() for _ in range(N+1)]
        indegree = [0] * (N+1)

        for i in range(N-1):
            for j in range(i+1, N):
                indegree[node_list[j]] += 1
                next_set[node_list[i]].add(node_list[j])

        M = int(next(iterator))
        for _ in range(M):
            a, b = int(next(iterator)), int(next(iterator))

            if b in next_set[a]:
                next_set[a].remove(b)
                next_set[b].add(a)
                indegree[a] += 1
                indegree[b] -= 1
            else:
                next_set[b].remove(a)
                next_set[a].add(b)
                indegree[b] += 1
                indegree[a] -= 1

        answer_list = []
        BFS = deque()

        for i in range(1, N+1):
            if not indegree[i]:
                BFS.append(i)
        
        while BFS:
            node = BFS.popleft()
            answer_list.append(node)

            for next_node in next_set[node]:
                indegree[next_node] -= 1

                if not indegree[next_node]:
                    BFS.append(next_node)
        
        if len(answer_list) == N:
            print(*answer_list)
        else:
            print("IMPOSSIBLE")


if __name__ == "__main__":
    solve()