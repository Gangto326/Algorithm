import sys

def solve():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    num_list = list(read().rstrip())

    stack = []
    count = K
    for num in num_list:
        while stack and stack[-1] < num and count:
            stack.pop()
            count -= 1

        stack.append(num)
    
    print("".join(stack[:-count]) if count else "".join(stack))

if __name__ == "__main__":
    solve()