import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)

    N = int(next(iterator))
    num_list = [int(next(iterator)) for _ in range(N)]
    stack = []

    answer = 0
    for i in range(N):
        num = num_list[i]

        while stack and stack[-1] <= num:
            stack.pop()

        answer += len(stack)
        stack.append(num)

    
    print(answer)


if __name__ == "__main__":
    solve()