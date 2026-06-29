import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    end = tuple(sorted(num_list))

    BFS = deque()
    BFS.append((tuple(num_list), 0))

    check = set()
    check.add(tuple(num_list))

    while BFS:
        comb, count = BFS.popleft()

        if comb == end:
            print(count)
            return
        
        comb_list = list(comb)
        for i in range(N):
            for j in range(i + 1, N):
                next_comb = comb_list[:]

                for k in range(j - i + 1):
                    next_comb[j - k] = comb_list[i + k]

                next_comb = tuple(next_comb)
                if not next_comb in check:
                    check.add(next_comb)
                    BFS.append((next_comb, count + 1))


if __name__ == "__main__":
    solve()