import sys
from collections import deque

def solve():
    num = int(sys.stdin.readline())

    BFS = deque()
    BFS.append(num)

    answer = 0
    while BFS:
        n = BFS.popleft()

        if n == 0:
            answer += 1
            continue

        if n >= 10 and 10 <= (n % 100) <= 34:
            BFS.append(n // 100)
        
        if n % 10 >= 1:
            BFS.append(n // 10)

    print(answer)


if __name__ == "__main__":
    solve()