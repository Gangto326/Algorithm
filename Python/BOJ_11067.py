import sys
from collections import defaultdict

def solve():
    read = sys.stdin.readline
    T = int(read())

    for tc in range(T):
        N = int(read())
        points = defaultdict(list)

        for _ in range(N):
            x, y = map(int, read().split())
            points[x].append(y)
        
        for i in points.keys():
            points[i].sort()
        
        stack = []
        for x in sorted(points.keys()):
            if not stack:
                if points[x][0] != 0:
                    for y in reversed(points[x]):
                        stack.append((x, y))
                else:
                    for y in points[x]:
                        stack.append((x, y))

            else:
                if stack[-1][1] == points[x][0]:
                    for y in points[x]:
                        stack.append((x, y))

                elif stack[-1][1] == points[x][-1]:
                    for y in reversed(points[x]):
                        stack.append((x, y))
                
                else:
                    stack.reverse()
        
        query_list = list(map(int, read().split()))
        M = query_list[0]
        for i in range(1, M+1):
            print(*stack[query_list[i]-1])


if __name__ == "__main__":
    solve()