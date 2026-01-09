import sys
from collections import deque

def solve():
    A, B = map(int, sys.stdin.readline().split())

    BFS = deque()
    BFS.append((A, 0, True))
    check = [[True, True] for _ in range(B+1)]

    while BFS:
        cost, count, chance = BFS.popleft()

        if cost+1 == B or cost*2 == B:
            print(count+1)
            break

        if chance:
            if check[cost+1][0]:
                check[cost+1][0] = False
                BFS.append((cost+1, count+1, chance))

            if cost * 2 < B and check[cost*2][0]:
                check[cost*2][0] = False
                BFS.append((cost*2, count+1, chance))

            if cost * 10 < B and check[cost*10][1]:
                check[cost*10][1] = False
                BFS.append((cost*10, count+1, False))

        else:
            if check[cost+1][1]:
                check[cost+1][1] = False
                BFS.append((cost+1, count+1, chance))

            if cost * 2 < B and check[cost*2][1]:
                check[cost*2][1] = False
                BFS.append((cost*2, count+1, chance))


if __name__ == "__main__":
    solve()