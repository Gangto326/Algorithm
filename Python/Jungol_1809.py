import sys

def solve():
    read = sys.stdin.readline
    N = int(read())
    num_list = [float('inf')] + list(map(int, read().split()))

    stack = [0]
    answer_list = [-1] * (N + 1)
    
    for i in range(1, N + 1):
        while num_list[stack[-1]] < num_list[i]:
            stack.pop()

        answer_list[i] = stack[-1]
        stack.append(i)

    print(" ".join(map(str, answer_list[1:])))


if __name__ == "__main__":
    solve()