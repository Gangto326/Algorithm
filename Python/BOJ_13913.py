import sys
from collections import deque

def solve():
    MAX_NUM = 100_000
    read = sys.stdin.readline
    N, K = map(int, read().split())

    BFS = deque()
    BFS.append((N, 0))
    check = [-1] * 100010
    check[N] = -2

    while BFS:
        location, count = BFS.popleft()

        if location == K:
            queue = deque()

            start = location
            while start != -2:
                queue.appendleft(start)
                start = check[start]

            print(count)
            print(*queue)
            return

        count += 1
        if location + 1 <= MAX_NUM and check[location + 1] == -1:
            check[location + 1] = location
            BFS.append((location + 1, count))

        if location - 1 >= 0 and check[location - 1] == -1:
            check[location - 1] = location
            BFS.append((location - 1, count))
        
        if location * 2 <= MAX_NUM and check[location * 2] == -1:
            check[location * 2] = location
            BFS.append((location * 2, count))


if __name__ == "__main__":
    solve()