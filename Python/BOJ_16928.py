import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N, M = map(int, read().split())
    jump_dict = {}

    for _ in range(N):
        start, end = map(int, read().split())
        jump_dict[start] = end
    
    for _ in range(M):
        start, end = map(int, read().split())
        jump_dict[start] = end

    check = [True] * 101
    BFS = deque()
    BFS.append((1, 0))

    while BFS:
        location, count = BFS.popleft()
        if location == 100:
            print(count)
            return

        count += 1
        for i in range(1, 7):
            next_location = location + i

            if next_location in jump_dict:
                next_location = jump_dict[next_location]

            if next_location < 1 or next_location > 100:
                continue
            
            if check[next_location]:
                check[next_location] = False
                BFS.append((next_location, count))


if __name__ == "__main__":
    solve()