import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = list(map(int, read().split()))
    answer_list = [-1] * N

    stack = []
    for i in range(N-1, -1, -1):
        while stack and stack[-1][0] <= num_list[i]:
            stack.pop()
        
        if not stack:
            answer_list[i] = -1
        else:
            answer_list[i] = stack[-1][0]
        stack.append((num_list[i], i))

    print(*answer_list)


if __name__ == "__main__":
    solve()