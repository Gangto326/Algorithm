import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    node_list = []

    for i in range(1, N + 1):
        PK, sub = map(int, read().split())
        node_list.append((i, PK, sub))
    
    node_list.sort(key = lambda x: x[1])

    stack = []
    parents = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i, PK, sub in node_list:
        last = None

        while stack and stack[-1][2] > sub:
            last = stack.pop()

        if last is not None:
            left[i] = last[0]
            parents[last[0]] = i
        
        if stack:
            right[stack[-1][0]] = i
            parents[i] = stack[-1][0]
        
        stack.append((i, PK, sub))

    print("YES")
    for i in range(1, N + 1):
        print(parents[i], left[i], right[i])


if __name__ == "__main__":
    solve()