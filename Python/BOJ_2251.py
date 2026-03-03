import sys
from collections import deque

def solve():
    read = sys.stdin.readline
    A, B, C = map(int, read().split())

    BFS = deque()
    BFS.append((0, 0, C))

    answer = set()
    check = set()

    while BFS:
        a, b, c = BFS.popleft()

        if a:
            a_to_b = B - b

            if a_to_b > a:
                a_to_b = a
            
            next_comb = (a - a_to_b, b + a_to_b, c)

            if not next_comb in check:
                check.add(next_comb)
                BFS.append(next_comb)
            
            a_to_c = C - c

            if a_to_c > a:
                a_to_c = a

            next_comb = (a - a_to_c, b, c + a_to_c)

            if not next_comb in check:
                check.add(next_comb)
                BFS.append(next_comb)

        if b:
            b_to_a = A - a

            if b_to_a > b:
                b_to_a = b
            
            next_comb = (a + b_to_a, b - b_to_a, c)

            if not next_comb in check:
                check.add(next_comb)
                BFS.append(next_comb)

            b_to_c = C - c

            if b_to_c > b:
                b_to_c = b

            next_comb = (a, b - b_to_c, c + b_to_c)

            if not next_comb in check:
                check.add(next_comb)
                BFS.append(next_comb)

        if c:
            c_to_a = A - a

            if c_to_a > c:
                c_to_a = c

            next_comb = (a + c_to_a, b, c - c_to_a)

            if not next_comb in check:
                check.add(next_comb)
                BFS.append(next_comb)

            c_to_b = B - b

            if c_to_b > c:
                c_to_b = c

            next_comb = (a, b + c_to_b, c - c_to_b)

            if not next_comb in check:
                check.add(next_comb)
                BFS.append(next_comb)
        
        if not a:
            answer.add(c)

    print(*sorted(list(answer)))


if __name__ == "__main__":
    solve()