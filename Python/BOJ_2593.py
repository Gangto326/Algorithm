import sys
from collections import deque

def solve():
    read = sys.stdin.buffer.readline
    N, M = map(int, read().split())
    elevator_list = [tuple(map(int, read().split())) for _ in range(M)]
    start, end = map(int, read().split())

    DP = [float('inf')] * (N + 1)
    DP[start] = 0

    check = [True] * M
    BFS = deque()
    BFS.append(start)

    root = [(-1, -1)] * (N + 1)
    while BFS:
        floor = BFS.popleft()
        
        if DP[end] != float('inf'):
            break

        next_cost = DP[floor] + 1
        for i in range(M):
            if check[i]:
                base_line, gap = elevator_list[i]
                
                if base_line > floor:
                    continue
                
                if not (floor - base_line) % gap:
                    check[i] = False

                    for j in range(base_line, N + 1, gap):
                        if DP[j] > next_cost:
                            DP[j] = next_cost
                            root[j] = (floor, i + 1)
                            BFS.append(j)
    
    if DP[end] == float('inf'):
        print(-1)
        
    else:
        print(DP[end])
        answer_list = []
        
        index = end
        while index != start:
            answer_list.append(str(root[index][1]))
            index = root[index][0]
        
        print("\n".join(reversed(answer_list)))


if __name__ == "__main__":
    solve()