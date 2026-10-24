import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    A, B, c, d = map(int, read().split())

    BFS = deque()
    check = set()

    BFS.append((0, 0, 0))
    check.add((0, 0))

    while BFS:
        a, b, count = BFS.popleft()
        
        if a == c and b == d:
            print(count)
            return

        if not (A, b) in check:
            BFS.append((A, b, count + 1))
            check.add((A, b))
        
        if not (a, B) in check:
            BFS.append((a, B, count + 1))
            check.add((a, B))
        
        if not (a, 0) in check:
            BFS.append((a, 0, count + 1))
            check.add((a, 0))

        if not (0, b) in check:
            BFS.append((0, b, count + 1))
            check.add((0, b))

        next_a, next_b = 0, 0

        if A - a >= b:
            next_a = a + b
            next_b = 0
        else:
            next_a = A
            next_b = b - (A - a)

        if not (next_a, next_b) in check:
            BFS.append((next_a, next_b, count + 1))
            check.add((next_a, next_b))
        
        next_a, next_b = 0, 0

        if B - b >= a:
            next_a = 0
            next_b = a + b
        else:
            next_a = a - (B - b)
            next_b = B
        
        if not (next_a, next_b) in check:
            BFS.append((next_a, next_b, count + 1))
            check.add((next_a, next_b))   

    print(-1)
    

if __name__ == "__main__":
    solve()