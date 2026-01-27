import sys
from collections import deque, defaultdict

def solve():
    MAX_SIZE = 100001

    read = sys.stdin.readline
    N, K = map(int, read().split())

    BFS = deque()
    BFS.append((N, 0))

    answer = MAX_SIZE
    way = 0
    check = [-1] * MAX_SIZE
    check[N] = 0

    while BFS:
        location, count = BFS.popleft()

        if count > answer:
            break

        if location == K:
            answer = count
            way += 1
            continue

        count += 1
        for next_location in (location-1, location+1, location*2):
            if 0 <= next_location < MAX_SIZE:
                if check[next_location] == -1 or check[next_location] >= count:
                    check[next_location] = count
                    BFS.append((next_location, count))

    print(answer)
    print(way)


if __name__ == "__main__":
    solve()